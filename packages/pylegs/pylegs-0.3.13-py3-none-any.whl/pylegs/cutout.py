"""
High-level interface to Legacy Survey data
"""


from io import BytesIO
from pathlib import Path
from time import sleep
from typing import List, Literal, Sequence, Tuple, Union

import numpy as np
import pandas as pd
import requests
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.io import fits
from astropy.units import Quantity
from PIL import Image

from pylegs.config import configs
from pylegs.io import (PathLike, PathOrFile, _is_folder, _prepare_path,
                       compress_fits_image, download_file,
                       parallel_function_executor)
from pylegs.pixscale import compute_pixscale_circle, compute_pixscale_ellip
from pylegs.utils import iauname, iauname_path


def _coord_to_deg(
  coord: int | float | Quantity | SkyCoord = None,
  ra: int | float | Quantity = None,
  dec: int | float | Quantity = None,
) -> Tuple[float, float]:
  if coord and isinstance(coord, SkyCoord):
    return coord.ra.to(u.deg).value, coord.dec.to(u.deg).value
  
  new_ra, new_dec = ra, dec
  if isinstance(ra, Quantity):
    new_ra = ra.to(u.deg).value
  
  if isinstance(dec, Quantity):
    new_dec = dec.to(u.deg).value
  
  return new_ra, new_dec


def cutout(
  coord: SkyCoord = None,
  ra: int | float | Quantity = None,
  dec: int | float | Quantity = None,
  save_path: PathOrFile = None,
  overwrite: bool = False,
  width: int = None,
  height: int = None,
  size: int = None,
  fmt: Literal['jpg', 'fits'] = 'jpg',
  bands: str = None,
  pixscale: float = 0.3,
  layer: str = 'ls-dr10',
  compress_type: Literal['RICE_1', 'RICE_ONE', 'PLIO_1', 'GZIP_1', 'GZIP_2', 'HCOMPRESS_1', 'NOCOMPRESS'] = 'NOCOMPRESS',
  hcomp_scale: int = 3,
  quantize_level: int = 10,
  quantize_method: Literal[-1, 1, 2] = -1,
  tile_shape: Tuple[int, int] = None,
  dither_seed: int = 0,
  http_client: requests.Session = None,
  dtype: Literal['bytes', 'numpy', 'pil', 'astropy'] = 'bytes'
) -> bytes | np.ndarray | Image.Image:
  """
  Downloads a single Legacy Survey object RGB stamp defined by RA and DEC.

  Parameters
  ----------
  ra: float
    Right ascension of the object.
  dec: float
    Declination of the object.
  save_path: pathlib.Path, optional
    Path where downloaded file will be stored.
  base_path: str, pathlib.Path, optional
    The path that will be appended at beggining of every paths if ``save_path``
    is ``None``.
  """
  if pixscale < 0 or pixscale > 100_000: return
  
  ra, dec = _coord_to_deg(coord=coord, ra=ra, dec=dec)
  
  if fmt[0] == '.': fmt = fmt[1:]
    
  if fmt == 'jpg':
    url = configs.CUTOUT_RGB_BASE_URL
  else:
    url = configs.CUTOUT_FITS_BASE_URL
    
  if size is not None:
    width, height = size, size
  else:
    if width is None or height is None:
      width, height = 300, 300
      
  _prepare_path(save_path)

  if _is_folder(save_path):
    save_path = iauname_path(
      iaunames=iauname(ra=ra, dec=dec),
      prefix=save_path,
      suffix=f'.{fmt}'
    )

  query_params = {
    'ra': ra,
    'dec': dec,
    'width': width,
    'height': height,
    'pixscale': pixscale,
    'layer': layer
  }
  
  if bands is not None:
    query_params = {**query_params, 'bands': bands}
 
  retry = 5
  attempt = 0
  while attempt < retry:
    try:
      image_bytes = download_file(
        url=url,
        query=query_params,
        save_path=save_path,
        http_client=http_client or configs.HTTP_CLIENT,
        overwrite=overwrite,
      )
      attempt += retry
    except:
      attempt += 1
      if attempt < retry:
        sleep(0.5)

  if compress_type is not None and compress_type.upper() != 'NOCOMPRESS':
    buffer = BytesIO(image_bytes)
    buffer.seek(0)
    compress_fits_image(
      file=buffer,
      compress_type=compress_type,
      hcomp_scale=hcomp_scale,
      quantize_level=quantize_level,
      quantize_method=quantize_method,
      tile_shape=tile_shape,
      dither_seed=dither_seed,
      ext=0,
      save_path=save_path,
      overwrite=overwrite,
    )
    
  if dtype.lower() == 'bytes':
    return image_bytes
  if dtype.lower() == 'pil':
    return Image.open(BytesIO(image_bytes))
  if dtype.lower() == 'numpy':
    return np.asarray(Image.open(BytesIO(image_bytes)))
  if dtype.lower() == 'astropy':
    return fits.open(BytesIO(image_bytes))



  
def batch_cutout(
  coords: SkyCoord = None,
  ra: Sequence[int | float | Quantity | SkyCoord] | SkyCoord | None = None,
  dec: Sequence[int | float | Quantity | SkyCoord] | SkyCoord | None = None,
  save_path: Sequence[PathLike] | PathLike | None = None,
  workers: int = 1,
  overwrite: bool = False,
  width: int | None = None,
  height: int | None = None,
  size: int | None = None,
  fmt: Literal['jpg', 'fits'] = 'jpg',
  bands: str | None = None,
  layer: str = 'ls-dr10',
  pixscale: Sequence[float | int] | float | Literal['auto'] = 0.3,
  shape_e1: Sequence[float] | None = None,
  shape_e2: Sequence[float] | None = None,
  shape_r: Sequence[float] | None = None,
  mag_r: Sequence[float] | None = None,
  pixscale_interpolation: Literal['step', 'linear'] = 'linear',
  compress_type: Literal['RICE_1', 'RICE_ONE', 'PLIO_1', 'GZIP_1', 'GZIP_2', 'HCOMPRESS_1', 'NOCOMPRESS'] = 'NOCOMPRESS',
  hcomp_scale: int = 3,
  quantize_level: int = 10,
  quantize_method: Literal[-1, 1, 2] = -1,
  tile_shape: Tuple[int, int] = None,
  dither_seed: int = 0,
  http_client: requests.Session | None = None,
) -> Tuple[List[Path], List[Path]]:
  """
  Downloads a list of objects defined by RA and DEC coordinates.

  The ``ra``, ``dec`` and ``save_path`` lists are mandatory and
  must have same length.

  Parameters
  ----------
  ra: List[float]
    The list of RA coordinates of the desired objects.
  dec: List[float]
    The list of DEC coordinates of the desired objects.
  save_path: List[Path], optional
    The list of path where files should be saved.
  base_path: str, Path, optional
    The path that will be appended at beggining of every paths if ``save_path``
    is ``None``.
  """
  ra, dec = _coord_to_deg(coord=coords, ra=ra, dec=dec)
  
  if _is_folder(save_path):
    save_path = iauname_path(
      iaunames=iauname(ra=ra, dec=dec),
      prefix=Path(save_path),
      suffix=f'.{fmt}'
    )

  params = [
    {
      'ra': _ra,
      'dec': _dec,
      'save_path': _save_path,
      'overwrite': overwrite,
      'width': width,
      'height': height,
      'size': size,
      'bands': bands,
      'layer': layer,
      'fmt': fmt,
      'compress_type': compress_type,
      'hcomp_scale': hcomp_scale,
      'quantize_level': quantize_level,
      'quantize_method': quantize_method,
      'tile_shape': tile_shape,
      'dither_seed': dither_seed,
      'http_client': http_client,
    }
    for _ra, _dec, _save_path in zip(ra, dec, save_path)
  ]
  
  if isinstance(pixscale, str) and pixscale == 'auto':
    if mag_r is None:
      raise ValueError('mag_r must be set to compute pixscale')
      
    if shape_r is not None:
      pixscale = compute_pixscale_circle(
        shape_r=shape_r, 
        size=size, 
        mag_r=mag_r, 
        interp=pixscale_interpolation,
      )
    elif shape_e1 is not None and shape_e2 is not None:
      pixscale = compute_pixscale_ellip(
        shape_e1=shape_e1, 
        shape_e2=shape_e2, 
        size=size, 
        mag_r=mag_r, 
        interp=pixscale_interpolation,
      )
    else:
      raise ValueError('set shape_e1 and shape_e2 for ellipse fit or shape_r for radial fit')
  
  if np.isscalar(pixscale):
    params = [{**_param, 'pixscale': pixscale} for _param in params]
  else:
    params = [{**_param, 'pixscale': _pixscale} for _param, _pixscale in zip(params, pixscale)]

  parallel_function_executor(
    cutout,
    params=params,
    workers=workers,
    unit='file',
    ignore_error=False,
  )

  success = [p for p in save_path if p.exists()]
  error = [p for p in save_path if not p.exists()]
  return success, error
    


if __name__ == '__main__':
  # ls = LegacyService(workers=6)
  # ls.batch_download_legacy_rgb(
  #   ra=[185.1458 + dx/2 for dx in range(20)],
  #   dec=[12.8624 + dy/2 for dy in range(20)],
  #   save_path=[Path(f'test/{i}.jpg') for i in range(20)]
  # )
  df = pd.DataFrame(({'ra':[184.4924, 184.4922], 'dec': [7.2737, 7.1862]}))
  cutout(ra=184.4924, dec=7.2737)
  # ls_crossmatch(df, ['mag_r', 'mag_g', 'mag_i', 'mag_z'], 3, 'test.csv')