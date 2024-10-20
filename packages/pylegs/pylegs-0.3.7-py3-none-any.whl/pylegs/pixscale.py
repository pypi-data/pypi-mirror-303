from argparse import ArgumentParser
from functools import cache, wraps
from inspect import getfullargspec
from pathlib import Path
from typing import Literal

import matplotlib
import numpy as np
import pandas as pd
from astromodule.io import read_image
from astropy import units as u
from matplotlib import pyplot as plt
from matplotlib.patches import Circle, Ellipse, Rectangle
from pixscale import compute_ellipse_bb, compute_ellipse_params
from scipy.interpolate import make_interp_spline
from tqdm import tqdm

from pylegs.config import configs
from pylegs.cutout import batch_cutout
from pylegs.io import read_table, write_table


def pseudo_vectorial(*vec_args):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      args_name = getfullargspec(func)[0]
      args_dict = {**dict(zip(args_name, args)), **kwargs}
                
      is_vector = False
      vec_len = -1
      for k in vec_args:
        is_vector = is_vector or not np.isscalar(args_dict[k])
        if is_vector:
          vec_len = len(args_dict[k])
      
      if is_vector:
        vec_iter = ({k: args_dict[k][i] for k in vec_args} for i in range(vec_len))
        scalar_args = {k: v for k, v in args_dict.items() if k not in vec_args}
        return np.asarray([
          func(**scalar_args, **_vector_args)
          for _vector_args in vec_iter
        ])
      return func(*args, **kwargs)
    return wrapper
  return decorator


def compute_ellipse_bb(x, y, major, minor, angle_deg):
  """
  Compute tight ellipse bounding box.
  
  see https://stackoverflow.com/questions/87734/how-do-you-calculate-the-axis-aligned-bounding-box-of-an-ellipse#88020
  """
  eps = 1e-10
  angle_rad = np.radians(angle_deg)
  angle_rad_eps = np.radians(angle_deg + eps)
  
  t = np.arctan(-minor / 2 * np.tan(angle_rad_eps) / (major / 2))
  [min_x, max_x] = np.sort([
    x + major / 2 * np.cos(t) * np.cos(angle_rad) - 
    minor / 2 * np.sin(t) * np.sin(angle_rad) 
    for t in (t, t + np.pi)
  ], axis=0)
  
  t = np.arctan(minor / 2 * 1. / np.tan(angle_rad_eps) / (major / 2))
  [min_y, max_y] = np.sort([
    y + minor / 2 * np.sin(t) * np.cos(angle_rad) +
    major / 2 * np.cos(t) * np.sin(angle_rad) 
    for t in (t, t + np.pi)
  ], axis=0)
  
  return min_x, min_y, max_x, max_y



# @pseudo_vectorial('shape_e1', 'shape_e2')
def compute_ellipse_params(shape_e1: float, shape_e2: float, max_e: float = None):
  eps = 1e-10
  e = np.sqrt(shape_e1 ** 2 + shape_e2 ** 2)
  if max_e is not None:
    e = np.minimum(e, max_e)
  b = 1 - e
  a = 1 + e
  angle = 180 - np.rad2deg(np.arctan2(shape_e2 + eps, shape_e1 + eps) / 2)
  mask = np.greater(b, a)
  if np.isscalar(mask):
    a, b = b, a
    angle += 180
  else:
    temp = a[mask]
    a[mask] = b[mask]
    b[mask] = temp
    angle[mask] += 180
  return a, b, angle



@cache
def _get_correction_factor_model(
  kind: Literal['circle', 'ellipse'], 
  interp: Literal['step', 'linear'],
  model: str | Path | pd.DataFrame = configs.CORRECTION_FACTOR,
):
  df = read_table(model)
  if kind.lower() == 'ellipse' and interp.lower() == 'step':
    return make_interp_spline(df.mag_r.values, df.cf_ellip_step.values, 0)
  elif kind.lower() == 'ellipse' and  interp.lower() == 'linear':
    return make_interp_spline(df.mag_r.values + 0.5, df.cf_ellip_linear.values, 1)
  elif kind.lower() == 'circle' and interp.lower() == 'step':
    return make_interp_spline(df.mag_r.values, df.cf_circ_step.values, 0)
  elif kind.lower() == 'circle' and interp.lower() == 'linear':
    return make_interp_spline(df.mag_r.values + 0.5, df.cf_circ_linear.values, 1)
  


def correction_factor_ellipse(
  mag_r: float, 
  interp: Literal['step', 'linear'] = 'linear'
):
  if interp == 'linear':
    return _get_correction_factor_model('ellipse', 'linear', configs.CORRECTION_FACTOR)(mag_r)
  return _get_correction_factor_model('ellipse', 'step', configs.CORRECTION_FACTOR)(mag_r)



def correction_factor_circle(
  mag_r: float, 
  interp: Literal['step', 'linear'] = 'linear'
):
  if interp == 'linear':
    return _get_correction_factor_model('circle', 'linear', configs.CORRECTION_FACTOR)(mag_r)
  return _get_correction_factor_model('circle', 'step', configs.CORRECTION_FACTOR)(mag_r)



# @pseudo_vectorial('shape_e1', 'shape_e2', 'mag_r')
def compute_fov_ellip(shape_e1, shape_e2, mag_r, interp):
  a, b, angle = compute_ellipse_params(shape_e1, shape_e2, 0.6)
  x0, y0, x1, y1 = compute_ellipse_bb(0, 0, b, a, angle)
  cf = correction_factor_ellipse(mag_r, interp=interp)
  width = np.abs(x1 - x0) * 2
  height = np.abs(y1 - y0) * 2
  return np.maximum(width, height) * cf * 60



# @pseudo_vectorial('shape_e1', 'shape_e2', 'mag_r')
def compute_pixscale_ellip(shape_e1, shape_e2, size, mag_r, interp):
  fov = compute_fov_ellip(shape_e1=shape_e1, shape_e2=shape_e2, mag_r=mag_r, interp=interp)
  return fov / size



# @pseudo_vectorial('shape_r', 'mag_r')
def compute_fov_circ(shape_r, mag_r, interp):
  cf = correction_factor_circle(mag_r, interp=interp)
  return 2 * shape_r * cf



# @pseudo_vectorial('shape_r', 'mag_r')
def compute_pixscale_circle(shape_r, size, mag_r, interp):
  fov = compute_fov_circ(shape_r=shape_r, mag_r=mag_r, interp=interp)
  return fov / size




def _crop_center(img, cropx, cropy):
  y, x, _ = img.shape
  startx = x/2 - (cropx/2)
  starty = y/2 - (cropy/2)
  return img[int(starty):int(starty+cropy),int(startx):int(startx+cropx)]


def _world2pix(value, pixscale):
  return value / pixscale


def draw_ellipse(
  shape_e1: float, 
  shape_e2: float, 
  pixscale: float, 
  size: float, 
  correction_factor: float,
  input_path: str | Path = None,
  ax: plt.Axes = None,
  output_path: str | Path = None,
  overwrite: bool = False,
):
  if output_path and Path(output_path).exists() and not overwrite: return
  
  a, b, angle = compute_ellipse_params(shape_e1, shape_e2, 0.6)
  b_pix = _world2pix(a, pixscale) * correction_factor * 60
  a_pix = _world2pix(b, pixscale) * correction_factor * 60
  
  x0, y0, x1, y1 = compute_ellipse_bb(0, 0, b, a, angle)
  width_pix = _world2pix(abs(x1 - x0), pixscale) * correction_factor * 60
  height_pix = _world2pix(abs(y1 - y0), pixscale) * correction_factor * 60
  
  l = max(width_pix, height_pix)
  center = size / 2
  
  if ax is None:
    fig, ax = plt.subplots()
  else:
    fig = ax.get_figure()
  
  if input_path is not None:
    img = read_image(input_path)
    ax.imshow(img)
    ax.axis('off')

  patch = Ellipse(
    xy=(center, center), 
    width=2*a_pix, 
    height=2*b_pix, 
    angle=angle, 
    color='tab:olive', 
    lw=2.5, 
    fill=False
  )
  ax.add_patch(patch)
  
  patch = Rectangle(
    xy=(center-l, center-l), 
    width=2*l, 
    height=2*l, 
    color='white', 
    lw=2.5, 
    fill=False
  )
  ax.add_patch(patch)
  
  patch = Rectangle(
    xy=(center-width_pix, center-height_pix), 
    width=2*width_pix, 
    height=2*height_pix, 
    color='cyan', 
    ls=':', 
    lw=2.5, 
    fill=False
  )
  ax.add_patch(patch)
  
  if output_path:
    fig.savefig(output_path, format='jpeg', pad_inches=0, bbox_inches='tight')
    plt.close(fig)
  
  
def draw_circle(
  shape_r: float,
  pixscale: float, 
  size: float, 
  correction_factor: float,
  input_path: str | Path = None,
  ax: plt.Axes = None,
  output_path: str | Path = None,
  overwrite: bool = False,
):
  if output_path and Path(output_path).exists() and not overwrite: return
  
  radius_pix = _world2pix(shape_r, pixscale) * correction_factor
  center = size / 2
  
  if ax is None:
    fig, ax = plt.subplots()
  else:
    fig = ax.get_figure()
  
  if input_path is not None:
    img = read_image(input_path)
    ax.imshow(img)
    ax.axis('off')

  patch = Circle(
    xy=(center, center), 
    radius=radius_pix, 
    color='tab:olive', 
    ls='-', 
    lw=2.5, 
    fill=False
  )
  ax.add_patch(patch)
  
  patch = Rectangle(
    xy=(center-radius_pix, center-radius_pix), 
    width=2*radius_pix, 
    height=2*radius_pix, 
    color='white', 
    lw=2.5, 
    fill=False
  )
  ax.add_patch(patch)
  
  if output_path:
    fig.savefig(output_path, format='jpeg', pad_inches=0, bbox_inches='tight')
    plt.close(fig)


  


if __name__ == '__main__':
  df = read_table('/home/natan/repos/legacy-stamps/samples/sample_10-11_300.csv')
  x = compute_pixscale_ellip(df.shape_e1.values, df.shape_e2.values, 300, df.mag_r.values, 'linear')
  y = df.pixscale_ellip_linear.values
  print(np.allclose(x, y))
  # print(compute_ellipse_bb(0, 0, 10, 15, 45))
  # print(compute_ellipse_bb(0, 0, np.asarray([10, 20]), np.asarray([15, 30]), np.asarray([45, -45])))