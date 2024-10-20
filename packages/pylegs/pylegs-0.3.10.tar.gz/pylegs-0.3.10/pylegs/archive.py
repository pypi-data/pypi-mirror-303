from abc import abstractmethod
from pathlib import Path
from shutil import move
from typing import Callable, Sequence, Tuple

import astropy.units as u
import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord, match_coordinates_sky
from astropy.coordinates.matrix_utilities import rotation_matrix
from astropy.coordinates.representation import UnitSphericalRepresentation
from astropy.io import fits
from astropy.table import Table, vstack
from astropy.units import Quantity, Unit
from astropy.utils.data import download_file
from astropy.visualization.wcsaxes import Quadrangle, SphericalCircle
from astropy.wcs import WCS
from matplotlib import pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon, Rectangle
from spherical_geometry.great_circle_arc import length
from spherical_geometry.polygon import SingleSphericalPolygon
from spherical_geometry.vector import radec_to_vector, vector_to_radec

from pylegs.config import configs
from pylegs.io import (PathLike, TableLike, parallel_function_executor,
                       read_table, write_table)
from pylegs.utils import guess_coords_columns, sanitize_quantity

__all__ = ['PolygonMatcher', 'RectangleMatcher', 'RadialMatcher', 'CrossMatcher']


def f1(ra1, dec1, ra2, dec2):
  _ra1 = np.deg2rad(ra1)
  _ra2 = np.deg2rad(ra2)
  _dec1 = np.deg2rad(dec1)
  _dec2 = np.deg2rad(dec2)
  return np.rad2deg(np.acos(np.sin(_dec1)*np.sin(_dec2) + np.cos(_dec1)*np.cos(_dec2)*np.abs(_ra1-_ra2)))
  
def f2(ra1, dec1, ra2, dec2):
  _ra1 = np.deg2rad(ra1)
  _ra2 = np.deg2rad(ra2)
  _dec1 = np.deg2rad(dec1)
  _dec2 = np.deg2rad(dec2)
  arg1 = np.sqrt(np.power(np.cos(_dec2)*np.sin(np.abs(_ra1-_ra2)), 2) + np.power(np.cos(_dec1)*np.sin(_dec2)-np.sin(_dec1)*np.cos(_dec2)*np.cos(np.abs(_ra1-_ra2)), 2))
  arg2 = np.sin(_dec1)*np.sin(_dec2) + np.cos(_dec1)*np.cos(_dec2)*np.cos(np.abs(_ra1-_ra2))
  return np.rad2deg(np.atan2(arg1, arg2))

def heaversine(ra1, dec1, ra2, dec2):
  _ra1 = np.deg2rad(ra1)
  _ra2 = np.deg2rad(ra2)
  _dec1 = np.deg2rad(dec1)
  _dec2 = np.deg2rad(dec2)
  x = np.sin(np.abs(_dec2-_dec1)/2)**2 + np.cos(_dec1)*np.cos(_dec2)*(np.sin(np.abs(_ra2-_ra1)/2)**2)
  return np.rad2deg(2*np.arcsin(np.sqrt(x)))

def _download_table(
  url: str, 
  output_path: str | Path, 
  columns: Sequence[str] = None, 
  brick_primary: bool = False,
  overwrite: bool = False,
  callback: Callable = None,
  compute_mag: Sequence[str] = None, # ['g', 'r', 'i', 'z', 'w1', 'w2', 'w3', 'w4']
):
  output_path = Path(output_path)
  if output_path.exists() and not overwrite: return
  path = download_file(url, cache=False, show_progress=False)
  move(path, output_path)
  if columns or brick_primary or callback or compute_mag:
    with fits.open(output_path) as hdul:
      table_data = hdul[1].data
    table = Table(data=table_data)
    if brick_primary:
      table = table[table['brick_primary'] == True]
    if compute_mag:
      for band in compute_mag:
        b = band.lower()
        if f'flux_{b}' in table.colnames:
          flux = table[f'flux_{b}'].value
          table[f'mag_{b}'] = np.where(flux > 0, 22.5 - 2.5 * np.log10(flux), -999)
    if callback is not None:
      table = callback(table)
    if columns:
      table = table[columns]
    table.write(output_path, overwrite=True)

  
class BaseArchiveMatcher:
  def __init__(self):
    self._wcs: WCS = None
    self._survey_bricks_df: pd.DataFrame = None
    self._intersection_df: pd.DataFrame = None
    
  @property
  @abstractmethod
  def wcs(self) -> WCS:
    pass
  
  @wcs.setter
  def wcs_setter(self, wcs: WCS):
    self._wcs = wcs
  
  @property
  @abstractmethod
  def intersection_df(self):
    pass
  
  @abstractmethod
  def _get_world_bounding_box(self, margin: float = 0.0) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    pass
  
  @abstractmethod
  def _plot_search_shape(self, ax = None, transform = None):
    pass
  
  @abstractmethod
  def _compute_brick_mask(self, ra1, ra2, dec1, dec2):
    pass
  
  @property
  def survey_bricks_df(self):
    if self._survey_bricks_df is None:
      # load north and south tables
      south_bricks = 'https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/survey-bricks-dr10-south.fits.gz'
      north_bricks = 'https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr9/north/survey-bricks-dr9-north.fits.gz'
      cols = ['brickname', 'ra', 'dec', 'ra1', 'dec1', 'ra2', 'dec2', 'survey_primary']
      south_table = read_table(south_bricks, columns=cols, fmt='fits', dtype='astropy')
      north_table = read_table(north_bricks, columns=cols, fmt='fits', dtype='astropy')
      
      # add hemisphere column
      south_table['hemisphere'] = ['south'] * len(south_table)
      north_table['hemisphere'] = ['north'] * len(north_table)
      
      # add dr column
      south_table['dr'] = [10] * len(south_table)
      north_table['dr'] = [9] * len(north_table)
      
      # concat tables
      bricks_table = vstack([north_table, south_table])
      
      # filter survey primary bricks
      bricks_table = bricks_table[bricks_table['survey_primary']]
      
      self._survey_bricks_df = bricks_table.to_pandas()
    return self._survey_bricks_df
  
  @survey_bricks_df.setter
  def survey_bricks_df_setter(self, df: pd.DataFrame):
    self._survey_bricks_df = df
  
  def _get_brick_urls(self, dr: Sequence[str], hemisphere: Sequence[str], brickname: Sequence[str]):
    base_url = 'https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/'
    url_pattern = base_url + 'dr{dr}/{h}/tractor/{prefix}/tractor-{brickname}.fits'
    prefix = [b[:3] for b in brickname]
    return [
      url_pattern.format(dr=_dr, h=_h, prefix=_prefix, brickname=_brickname)
      for _dr, _h, _prefix, _brickname in zip(dr, hemisphere, prefix, brickname)
    ]
    
  def download_bricks(
    self, 
    bricks_dir: PathLike = 'legacy_bricks',
    columns: Sequence[str] = None,
    brick_primary: bool = True,
    filter_function: Callable = None,
    compute_mag: Sequence[str] = None,
    overwrite: bool = False,
    workers: int = 1,
  ):
    bricks_dir = Path(bricks_dir)
    bricks_dir.mkdir(parents=True, exist_ok=True)
    download_df = self.intersection_df.copy(deep=True)
    download_df['local_path'] = [bricks_dir / f'{b}.fits' for b in download_df.brickname]
    
    if not overwrite:
      overwrite_mask = np.array([p.exists() for p in download_df.local_path])
      download_df = download_df.iloc[~overwrite_mask]
    
    if len(download_df) > 0:
      download_df['url'] = self._get_brick_urls(
        dr=download_df['dr'].values, 
        hemisphere=download_df.hemisphere.values, 
        brickname=download_df.brickname.values
      )
      args = [
        {
          'url': row.url,
          'output_path': row.local_path,
          'columns': columns,
          'brick_primary': brick_primary,
          'overwrite': overwrite,
          'callback': filter_function,
          'compute_mag': compute_mag,
        }
        for i, row in download_df.iterrows()
      ]
      parallel_function_executor(
        func=_download_table, 
        params=args, 
        workers=workers,
        unit='table',
        progress=True,
      )
  
  def match(
    self, 
    output_path: PathLike,
    bricks_dir: PathLike = 'legacy_bricks',
    columns: Sequence[str] = None,
    overwrite: bool = False,
    include_brickname: bool = False,
    include_dr: bool = False,
  ) -> Table:
    output_path = Path(output_path)
    bricks_dir = Path(bricks_dir)
    if output_path.exists() and not overwrite: 
      return
    
    df = self.intersection_df
    
    concat = None
    first_write = True
    for i, row in df.iterrows():
      # load downloaded brick table
      brick_table = read_table(bricks_dir / f'{row.brickname}.fits', dtype='astropy')
      
      # filter columns
      if columns:
        brick_table = brick_table[columns]
      
      # filter rows in bricks at border to match input shape
      if not row.full_intersection:
        coords = SkyCoord(ra=brick_table['ra'].value, dec=brick_table['dec'].value, unit=u.deg, frame='icrs')
        mask = self._compute_brick_mask(coords, ra1=row.ra1, ra2=row.ra2, dec1=row.dec1, dec2=row.dec2)
        brick_table = brick_table[mask]
      
      # include brick name column
      if include_brickname:
        brick_table['brickname'] = [row.brickname] * len(brick_table)
      
      # include data release column
      if include_dr:
        brick_table['dr'] = [row.dr] * len(brick_table)
      
      # concatenate tables
      if len(brick_table) > 0:
        if first_write:
          concat = brick_table
          first_write = False
        else:
          concat = vstack([concat, brick_table])
      
    # write table in output_path
    if concat:
      write_table(concat, output_path)
    return concat
    
  def plot(
    self, 
    labels: bool = True, 
    show: bool = True, 
    ax = None,
    title: str = 'Legacy Archive Search',
    tick_size: float = 10,
    label_size: float = 10,
    label_alpha: float = 0.8,
    invert_ra: bool = True,
    ra_unit: str = 'hourangle',
    dec_unit: str = 'deg',
    ra_decimal: bool = False,
    dec_decimal: bool = False,
    xticks: Sequence[float] | Quantity = None,
    yticks: Sequence[float] | Quantity = None,
    dpi: int = 150,
    figsize: Tuple[float, float] = (6, 5),
    xlabel: str = 'RA',
    ylabel: str = 'DEC',
    xlim: Tuple[float | float] | Quantity = None,
    ylim: Tuple[float | float] | Quantity = None,
    xpad: float | Quantity = 0 * u.deg,
    ypad: float | Quantity = 0 * u.deg,
  ):
    # configure axes and transforms
    if ax is None:
      fig = plt.figure(figsize=figsize, dpi=dpi)
      ax = fig.add_subplot(projection=self.wcs)

    # plot legacy survey bricks
    df = self.intersection_df
    anchors = [(ra1, dec1) for ra1, dec1 in zip(df.ra1.values, df.dec1.values)]
    widths = (df.ra2 - df.ra1).abs().values
    heights = (df.dec2 - df.dec1).abs().values
    bricks_rects = [
      Rectangle(xy=a, width=w, height=h)
      for a, w, h in zip(anchors, widths, heights)
    ]
    pc = PatchCollection(
      bricks_rects, 
      facecolor=(31/255, 119/255, 180/255, 0.5),
      edgecolor=(31/255, 119/255, 180/255, 0.75),
      transform=ax.get_transform('icrs'),
    )
    ax.add_collection(pc)
    
    # plot input search shape
    self._plot_search_shape(ax=ax, transform=ax.get_transform('icrs'))
    
    # plot brick names
    if labels:
      bricks_center_coords = SkyCoord(ra=df.ra.values, dec=df.dec.values, unit=u.deg)
      x_arr, y_arr = self.wcs.world_to_pixel(bricks_center_coords)

      for name, _x, _y in zip(df.brickname.values, x_arr, y_arr):
        name = name[:4] + '\n' + name[4:]
        ax.annotate(
          text=name, 
          xy=(_x, _y), 
          xycoords='data',
          fontsize=7, 
          ha='center', 
          va='center',
          alpha=label_alpha,
          transform=ax.get_transform('icrs'),
        )
    
    # plot grid
    ax.coords.grid(linestyle=':', color='tab:gray', alpha=0.55)
    
    # configure axis units
    ax.coords[0].set_format_unit(ra_unit, decimal=ra_decimal)
    ax.coords[1].set_format_unit(dec_unit, decimal=dec_decimal)
    
    # configure axis limit
    xpad, ypad = sanitize_quantity((xpad, ypad), u.deg, convert=True)
    ra_min = np.minimum(df.ra1.min(), df.ra2.min())*u.deg - xpad
    ra_max = np.maximum(df.ra1.max(), df.ra2.max())*u.deg + xpad
    dec_min = np.minimum(df.dec1.min(), df.dec2.min())*u.deg - ypad
    dec_max = np.maximum(df.dec1.max(), df.dec2.max())*u.deg + ypad
    xlim = xlim or Quantity([ra_min, ra_max])
    ylim = ylim or Quantity([dec_min, dec_max])
    xlim = sanitize_quantity(xlim, u.deg, convert=True)
    ylim = sanitize_quantity(ylim, u.deg, convert=True)
    xlim_pix, ylim_pix = self.wcs.world_to_pixel(SkyCoord(ra=xlim, dec=ylim))
    if invert_ra:
      ax.set_xlim(xlim_pix[1], xlim_pix[0])
    else:
      ax.set_xlim(*xlim_pix)
    ax.set_ylim(*ylim_pix)
    
    # configure ticks
    ax.tick_params(direction='in', labelsize=tick_size)
    if xticks is not None:
      ax.coords[0].set_ticks(sanitize_quantity(xticks, u.deg, convert=True))
    if yticks is not None:
      ax.coords[1].set_ticks(sanitize_quantity(yticks, u.deg, convert=True))
    
    # configure labels
    ax.coords[0].set_auto_axislabel(False)
    ax.coords[0].set_axislabel(xlabel, fontsize=label_size)
    ax.coords[1].set_auto_axislabel(False)
    ax.coords[1].set_axislabel(ylabel, fontsize=label_size)
    
    if title:
      ax.set_title(title)

    if show: 
      plt.show()
    return ax
      


class PolygonMatcher(BaseArchiveMatcher):
  def __init__(
    self, 
    coords: SkyCoord = None, 
    ra: Sequence[float] | Quantity = None, 
    dec: Sequence[float] | Quantity = None,
  ):
    super().__init__()
    if isinstance(coords, SkyCoord):
      self.coords = coords
    elif ra is not None and dec is not None:
      ra, dec = sanitize_quantity((ra, dec), u.deg)
      self.coords = SkyCoord(ra=ra, dec=dec)
    else:
      raise ValueError('Either `coords` or `ra` and `dec` must be passed')
    self._ra_lim = None
    self._dec_lim = None
    self._search_polygon = None
    
  @property
  def wcs(self) -> WCS:
    if self._wcs is None:
      (ra_min, ra_max), (dec_min, dec_max) = self._get_world_bounding_box()
      center = [ra_min + abs(ra_max-ra_min)/2, dec_min + abs(dec_max-dec_min)/2]
      self._wcs = WCS(naxis=2)
      self._wcs.wcs.crpix = center
      self._wcs.wcs.cdelt = [-1, 1]
      self._wcs.wcs.crval = center 
      self._wcs.wcs.ctype = ['RA---TAN', 'DEC--TAN']
    return self._wcs
  
  @property
  def search_polygon(self):
    if self._search_polygon is None:
      points = np.array(radec_to_vector(self.coords.ra.deg, self.coords.dec.deg)).T
      self._search_polygon = SingleSphericalPolygon(points)
    return self._search_polygon
  
  @property
  def intersection_df(self):
    if self._intersection_df is None:
      ra_lim, dec_lim = self._get_world_bounding_box(1.5)
      df = self.survey_bricks_df
      df = df[df.ra.between(*ra_lim) & df.dec.between(*dec_lim)]
      df = df.reset_index(drop=True)
      
      # A = np.array(radec_to_vector(self.coords.ra.deg, self.coords.dec.deg)).T
      # pol = SingleSphericalPolygon(A)
      intersection_mask = np.empty(shape=(len(df),), dtype=bool)
      full_intersection_mask = np.empty(shape=(len(df),), dtype=bool)
      for i, row in df.iterrows():
        ra_boundings = [row.ra1, row.ra2, row.ra2, row.ra1]
        dec_boundings = [row.dec1, row.dec1, row.dec2, row.dec2]
        poly_3d = np.array(radec_to_vector(ra_boundings, dec_boundings)).T
        inside_3d = radec_to_vector(row.ra, row.dec)
        brick_pol = SingleSphericalPolygon(poly_3d, inside_3d)
        intersection_mask[i] = brick_pol.intersects_poly(self.search_polygon)
        full_intersection_mask[i] = brick_pol.overlap(self.search_polygon) > .999
      df['full_intersection'] = full_intersection_mask
      self._intersection_df = df.iloc[intersection_mask].reset_index(drop=True)
    return self._intersection_df

  def _get_world_bounding_box(self, margin: float = 0):
    if self._ra_lim is None or self._dec_lim is None:
      self._ra_lim = self.coords.ra.deg.min(), self.coords.ra.deg.max()
      self._dec_lim = self.coords.dec.deg.min(), self.coords.dec.deg.max()
    ra_lim = (self._ra_lim[0] - margin, self._ra_lim[1] + margin)
    dec_lim = (self._dec_lim[0] - margin, self._dec_lim[1] + margin)
    return ra_lim, dec_lim
  
  def _compute_brick_mask(
    self, 
    coords: SkyCoord, 
    ra1: float, 
    ra2: float, 
    dec1: float, 
    dec2: float
  ):
    search_box_3d = np.array(radec_to_vector(
      [ra1, ra2, ra2, ra1], [dec1, dec1, dec2, dec2]
    )).T
    inside = radec_to_vector(ra1 + abs(ra2-ra1)/2, dec1 + abs(dec2-dec1)/2)
    brick_pol = SingleSphericalPolygon(search_box_3d, inside)
    intersection_pol = brick_pol.intersection(self.search_polygon)
    return np.array([
      intersection_pol.contains_radec(_ra, _dec, degrees=True) 
      for _ra, _dec in zip(coords.ra.deg, coords.dec.deg)
    ])
  
  def _plot_search_shape(self, ax = None, transform = None):
    points = np.array(list(zip(self.coords.ra.deg, self.coords.dec.deg)))
    poly = Polygon(
      points,
      linewidth=2, 
      facecolor=(31/255, 119/255, 180/255, 0.55), # tab:blue
      edgecolor=(214/255, 39/255, 40/255, 0.75), # tab:red
      transform=transform
    )
    ax.add_patch(poly)
  
  

class RectangleMatcher(PolygonMatcher):
  def __init__(
    self, 
    ra1: float | Quantity, 
    ra2: float | Quantity, 
    dec1: float | Quantity, 
    dec2: float | Quantity
  ):
    ra1, ra2, dec1, dec2 = sanitize_quantity((ra1, ra2, dec1, dec2), u.deg)
    coords = SkyCoord(ra=[ra1, ra2, ra2, ra1], dec=[dec1, dec1, dec2, dec2])
    super().__init__(coords)



class RadialMatcher(BaseArchiveMatcher):
  def __init__(
    self, 
    center: SkyCoord = None, 
    ra: float | Quantity = None, 
    dec: float | Quantity = None, 
    radius: float | Quantity = None,
  ):
    super().__init__()
    if isinstance(center, SkyCoord):
      self.center = center
    elif ra is not None and dec is not None:
      ra, dec = sanitize_quantity((ra, dec), u.deg)
      self.center = SkyCoord(ra=ra, dec=dec)
    else:
      raise ValueError('Either `center` or `ra` and `dec` must be passed')
    self.radius = sanitize_quantity(radius, u.deg)
    self._ra_lim = None
    self._dec_lim = None
    
  @property
  def wcs(self) -> WCS:
    if self._wcs is None:
      self._wcs = WCS(naxis=2)
      self._wcs.wcs.cdelt = [-1, 1]
      self._wcs.wcs.crval = [self.center.ra.deg, self.center.dec.deg] 
      self._wcs.wcs.ctype = ['RA---TAN', 'DEC--TAN']
    return self._wcs
    # if self._wcs is None:
    #   self._wcs = WCS(naxis=2)
    #   self._wcs.wcs.crpix = [self.ra, self.dec] # (size - 1) / 2
    #   self._wcs.wcs.cdelt = np.array([-1, 1]) # resolution.to(u.deg).value
    #   self._wcs.wcs.crval = [self.ra, self.dec] 
    #   self._wcs.wcs.ctype = ['RA---TAN', 'DEC--TAN']
    # return self._wcs
    
  @property
  def intersection_df(self):
    if self._intersection_df is None:
      ra, dec = self.survey_bricks_df.ra.values, self.survey_bricks_df.dec.values
      bricks_centers = SkyCoord(ra=ra, dec=dec, unit=u.deg, frame='icrs')
      mask = self.center.separation(bricks_centers) < (self.radius + 1.5*u.deg)
      df = self.survey_bricks_df.iloc[mask].copy()
      
      point_intersection_mask = np.empty(shape=(len(df), 4))
      points = [('ra1', 'dec1'), ('ra2', 'dec1'), ('ra2', 'dec2'), ('ra1', 'dec2')]
      # center_vec = np.repeat([radec_to_vector(self.ra, self.dec)], len(df), axis=0) # shape: N,3
      for i, p in enumerate(points):
        s = SkyCoord(ra=df[p[0]].values, dec=df[p[1]].values, unit=u.deg, frame='icrs')
        point_intersection_mask[:, i] = self.center.separation(s) < self.radius
        # point_intersection_mask[:, i] = heaversine(self.ra, self.dec, s.ra.deg, s.dec.deg)*u.deg < self.radius
        # point_intersection_mask[:, i] = f2(self.ra, self.dec, s.ra.deg, s.dec.deg)*u.deg < self.radius
        # bricks_centers_vec = np.array(radec_to_vector(df[p[0]].values, df[p[1]].values)).T # shape: N,3
        # sep = length(center_vec, bricks_centers_vec) * 180 / np.pi
        # point_intersection_mask[:, i] = sep * u.deg < (self.radius * u.deg + 1*u.deg)
        
      intersection_mask = point_intersection_mask.any(axis=-1)
      full_intersection_mask = point_intersection_mask.all(axis=-1)
      df['full_intersection'] = full_intersection_mask
      self._intersection_df = df.iloc[intersection_mask].reset_index(drop=True)
    return self._intersection_df
  
  def _get_world_bounding_box(self, margin: float = 0) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    if self._ra_lim is None or self._dec_lim is None:
      # ra_min = np.minimum(self.intersection_df.ra1.min(), self.intersection_df.ra2.min())
      # ra_max = np.maximum(self.intersection_df.ra1.max(), self.intersection_df.ra2.max())
      # dec_min = np.minimum(self.intersection_df.dec1.min(), self.intersection_df.dec2.min())
      # dec_max = np.minimum(self.intersection_df.dec1.max(), self.intersection_df.dec2.max())
      # self._ra_lim = (ra_min, ra_max)
      # self._dec_lim = (dec_min, dec_max)
      
      # search_circle = SphericalCircle(
      #   center=[self.ra, self.dec]*u.deg,
      #   radius=self.radius*u.deg,
      # )
      # p = search_circle.get_path()
      # print(dir(p))
      
      # ra = self.ra * u.deg
      # dec = self.dec * u.deg
      # r = self.radius * u.deg
      # sep_dec = SkyCoord(ra=ra-r, dec=dec).separation(SkyCoord(ra=ra+r, dec=dec))
      # sep_ra = SkyCoord(ra=ra, dec=dec-r).separation(SkyCoord(ra=ra, dec=dec+r))
      # print('sep_r =',sep_ra.deg)
      # print('sep_d =',sep_dec.deg)
      # self._ra_lim = ((ra - sep_ra).deg, (ra + sep_ra).deg)
      # self._dec_lim = ((dec - sep_dec).deg, (dec + sep_dec).deg)
      
      self._ra_lim = self.ra - self.radius, self.ra + self.radius
      self._dec_lim = self.dec - self.radius, self.dec + self.radius
      
      # lon = np.array([0, np.pi/2, np.pi, -np.pi/2]) * u.rad
      # lat = np.repeat([np.pi/2 - np.deg2rad(self.radius)], 4) * u.rad
      # center = SkyCoord(ra=self.ra, dec=self.dec, unit=u.deg)
      # center_lon, center_lat = center.spherical.lon, center.spherical.lat
      # lon, lat = self._rotate_polygon(lon, lat, center_lon, center_lat)
      # lon = lon.to(u.deg).value
      # lat = lat.to(u.deg).value
      # print(lon)
      # print(lat)
      # print(np.array([lon, lat]).T)
      
    # print(self._ra_lim, self._dec_lim)
    # return (lon.min() - margin, lon.max() - margin), (lat.min() - margin, lat.max() + margin)
    return (self._ra_lim[0] - margin, self._ra_lim[1] + margin), (self._dec_lim[0] - margin, self._dec_lim[1] + margin) 
  
  def _plot_search_shape(self, ax=None, transform=None):
    # plot circle
    search_circle = SphericalCircle(
      center=[self.center.ra, self.center.dec],
      radius=self.radius,
      linewidth=2,
      facecolor=(31/255, 119/255, 180/255, 0.55), # tab:blue
      edgecolor=(214/255, 39/255, 40/255, 0.75), # tab:red
      transform=transform,
    )
    ax.add_patch(search_circle)

    # plot center
    ax.scatter(
      x=self.center.ra.deg, 
      y=self.center.dec.deg, 
      s=30, 
      c='tab:red', 
      marker='+', 
      alpha=0.75, 
      transform=transform, 
    )
    
  def _compute_brick_mask(self, coords: SkyCoord, **kwargs):
    return coords.separation(self.center) < self.radius
    
  def _rotate_polygon(self, lon, lat, lon0, lat0):
    """
    Given a polygon with vertices defined by (lon, lat), rotate the polygon
    such that the North pole of the spherical coordinates is now at (lon0,
    lat0). Therefore, to end up with a polygon centered on (lon0, lat0), the
    polygon should initially be drawn around the North pole.
    """
    # Create a representation object
    polygon = UnitSphericalRepresentation(lon=lon, lat=lat)

    # Determine rotation matrix to make it so that the circle is centered
    # on the correct longitude/latitude.
    transform_matrix = rotation_matrix(-lon0, axis="z") @ rotation_matrix(
        -(0.5 * np.pi * u.radian - lat0), axis="y"
    )

    # Apply 3D rotation
    polygon = polygon.to_cartesian()
    polygon = polygon.transform(transform_matrix)
    polygon = UnitSphericalRepresentation.from_cartesian(polygon)

    return polygon.lon, polygon.lat



class CrossMatcher(BaseArchiveMatcher):
  def __init__(
    self, 
    coords: SkyCoord = None, 
    ra: Sequence[float] | Quantity = None,
    dec: Sequence[float] | Quantity = None,
    radius: Quantity = 1 * u.arcsec,
  ):
    super().__init__()
    if isinstance(coords, SkyCoord):
      self.coords = coords
    elif ra is not None and dec is not None:
      ra, dec = sanitize_quantity((ra, dec), u.deg)
      self.coords = SkyCoord(ra=ra, dec=dec)
    else:
      raise ValueError('Either `coords` or `ra` and `dec` must be passed')
    self.radius = sanitize_quantity(radius, u.deg)
    self._ra_lim = None
    self._dec_lim = None
    
  @classmethod
  def from_table(
    cls, 
    table: TableLike, 
    radius: Quantity = 1 * u.arcsec,
    ra_col: str = None, 
    dec_col: str = None, 
    fmt: str = None,
    unit: str = 'deg',
  ):
    df = read_table(table, fmt=fmt)
    ra_col, dec_col = guess_coords_columns(df, ra_col, dec_col)
    coords = SkyCoord(ra=df[ra_col].values, dec=df[dec_col].values, unit=unit)
    return cls(coords=coords, radius=radius)
  
  @property
  def wcs(self) -> WCS:
    if self._wcs is None:
      (ra_min, ra_max), (dec_min, dec_max) = self._get_world_bounding_box()
      center = [ra_min + abs(ra_max-ra_min)/2, dec_min + abs(dec_max-dec_min)/2]
      self._wcs = WCS(naxis=2)
      self._wcs.wcs.crpix = center
      self._wcs.wcs.cdelt = [-1, 1]
      self._wcs.wcs.crval = center
      self._wcs.wcs.ctype = ['RA---TAN', 'DEC--TAN']
    return self._wcs
  
  @property
  def intersection_df(self):
    if self._intersection_df is None:
      bricks_df = self.survey_bricks_df
      bricks_coords = SkyCoord(
        ra=bricks_df.ra.values, 
        dec=bricks_df.dec.values, 
        unit=u.deg
      )
      max_it = 30
      it = 1
      n_objects = len(self.coords)
      n_objects_found = 0
      bricks_idx = np.array([])
      while n_objects_found < n_objects and it < max_it:
        idx, _, _ = match_coordinates_sky(self.coords, bricks_coords, it)
        candidates_df = bricks_df.iloc[idx]
        ra1 = candidates_df.ra1.values
        ra2 = candidates_df.ra2.values
        dec1 = candidates_df.dec1.values
        dec2 = candidates_df.dec2.values
        mask = (
          (np.minimum(ra1, ra2) < self.coords.ra.deg) & 
          (self.coords.ra.deg < np.maximum(ra1, ra2)) & 
          (np.minimum(dec1, dec2) < self.coords.dec.deg) & 
          (self.coords.dec.deg < np.maximum(dec1, dec2))
        )
        bricks_idx = np.concatenate((bricks_idx, idx[mask]))
        n_objects_found += np.count_nonzero(mask)
        it += 1
      self._intersection_df = bricks_df.iloc[np.unique(bricks_idx)].reset_index(drop=True)
    return self._intersection_df
  
  # @property
  # def intersection_df(self):
  #   all_points_3d = radec_to_vector(self.coords.ra.deg, self.coords.dec.deg, degrees=True)
  #   search_pol = SingleSphericalPolygon.convex_hull(all_points_3d)
  #   hull_3d = search_pol.points
  #   hull_ra, hull_dec = vector_to_radec(x=hull_3d[:, 0], y=hull_3d[:, 1], z=hull_3d[:, 2])
  #   pol_coords = SkyCoord(ra=hull_ra, dec=hull_dec, unit=u.deg)
  #   pol_matcher = PolygonMatcher(pol_coords)
  #   pol_matcher._search_polygon = search_pol
  #   intersection_df = pol_matcher.intersection_df
  
  def _get_world_bounding_box(self, margin: float = 0) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    if self._ra_lim is None or self._dec_lim is None:
      self._ra_lim = self.coords.ra.deg.min(), self.coords.ra.deg.max()
      self._dec_lim = self.coords.dec.deg.min(), self.coords.dec.deg.max()
    return (self._ra_lim[0] - margin, self._ra_lim[1] + margin), (self._dec_lim[0] - margin, self._dec_lim[1] + margin)
  
  def _plot_search_shape(self, ax=None, transform=None):
    ax.scatter(
      self.coords.ra.deg,
      self.coords.dec.deg,
      s=10,
      c='tab:red',
      alpha=0.75,
      transform=transform,
    )
    
  def _compute_brick_mask(self, coords: SkyCoord, **kwargs):
    _, sep, _ = match_coordinates_sky(coords, self.coords)
    return sep < self.radius



if __name__ == '__main__':
  RadialMatcher(ra=120.2939, dec=40.7714, radius=1).plot(labels=False)
  
  # PolygonMatcher(SkyCoord(ra=[119, 121, 121, 119], dec=[50, 50, 51, 51], unit=u.deg)).plot()
  
  # r = RectangleMatcher(119, 119.5, 50, 51)
  # r.plot()
  # r.download_bricks(columns=['ra', 'dec', 'brick_primary'], brick_primary=True, workers=2)
  # r.download_objects('legacy_bricks/test.fits', workers=4, overwrite=True)
  
  # m = CrossMatcher(SkyCoord(ra=[119.1111, 119.1187, 119.54], dec=[50.4040, 50.4010, 50.06], unit=u.deg))
  # m.plot()