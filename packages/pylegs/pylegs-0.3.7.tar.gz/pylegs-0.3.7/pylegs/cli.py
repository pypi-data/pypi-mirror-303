from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Sequence

import numpy as np
import yaml
from astropy import units as u

from pylegs.config import configs
from pylegs.io import read_table
from pylegs.utils import guess_coords_columns


def _is_numeric(value: str):
  try:
    float(value)
    return True
  except ValueError:
    return False


def handle_dlcat(args: Namespace):
  from pylegs.tap import download_catalog
  
  if args.types:
    exclude = {'PSF', 'REX', 'DEV', 'EXP', 'SER', 'DUP'} - set([s.upper() for s in args.types])
  else:
    exclude = None

  download_catalog(
    save_path=args.output,
    columns=args.cols,
    ra_min=args.ramin,
    ra_max=args.ramax,
    delta_ra=args.delta,
    table=args.table,
    exclude_types=exclude,
    magr_min=args.rmin,
    magr_max=args.rmax,
    dec_min=args.decmin,
    dec_max=args.decmax,
    brick_primary=args.primary,
    overwrite=args.overwrite,
    workers=args.workers,
    tmp_folder=args.tmp,
    overwrite_tmp=args.otmp,
  )
  
def handle_cutout(args: Namespace):
  from pylegs.cutout import batch_cutout
  
  cols = []
  if args.ra is not None:
    cols.append(args.ra)
  if args.dec is not None:
    cols.append(args.dec)
  if not _is_numeric(args.pixscale) and args.pixscale != 'auto':
    cols.append(args.pixscale)
  
  df = read_table(args.cat, columns=cols or None)
  if args.limit is None:
    df = df.iloc[args.offset:]
  else:
    df = df.iloc[args.offset:args.limit]
  
  ra_col, dec_col = guess_coords_columns(df, args.ra, args.dec)
  ra = df[ra_col].values * u.deg
  dec = df[dec_col].values * u.deg
  shape_e1 = None
  shape_e2 = None
  shape_r = None
  mag_r = None
  if args.pixscale == 'auto':
    pixscale = 'auto'
    mag_r = df[args.magr].values
    if args.shape1 is not None and args.shape2 is not None:
      shape_e1 = df[args.shape1].values
      shape_e2 = df[args.shape2].values
    elif args.shaper is not None:
      shape_r = df[args.shaper].values
  elif _is_numeric(args.pixscale):
    pixscale = float(args.pixscale)
  else:
    pixscale = df[args.pixscale].values
  
  save_path = Path(args.output)
  if args.fnames is not None:
    save_path = [save_path / f'{f}.{args.format}' for f in df[args.fnames].values]
  
  batch_cutout(
    ra=ra,
    dec=dec,
    pixscale=pixscale,
    save_path=save_path,
    workers=args.workers,
    overwrite=args.overwrite,
    width=args.width,
    height=args.height,
    size=args.size,
    shape_e1=shape_e1,
    shape_e2=shape_e2,
    shape_r=shape_r,
    mag_r=mag_r,
    fmt=args.format,
    bands=args.bands,
    layer=args.layer,
    compress_type=args.compress,
    quantize_level=args.quantize_level,
    quantize_method=args.quantize_method,
    tile_shape=args.tile_shape,
    dither_seed=args.dither_seed,
    hcomp_scale=args.hcomp_scale,
    pixscale_interpolation=args.pixscale_interp,
  )
  

def handle_axmatch(args: Namespace):
  from pylegs.archive import CrossMatcher
  
  cm = CrossMatcher.from_table(
    table=args.input, 
    radius=args.radius, 
    ra_col=args.ra, 
    dec_col=args.dec, 
    fmt=args.fmt,
    unit=args.unit,
  )
  cm.match(
    output_path=args.output,
    bricks_dir=args.cache,
    columns=args.columns,
    overwrite=args.overwrite,
    include_brickname=args.brickname,
    include_dr=args.dr,
  )
  
  
  
def handle_xmatch(args: Namespace):
  from pylegs.tap import dl_crossmatch
  
  df = read_table(args.input)
  ra_col, dec_col = guess_coords_columns(df, args.tabra, args.tabdec)
  
  mask = np.ones(shape=(len(df),), dtype=bool)
  if args.ramin is not None:
    mask &= df[ra_col] > args.ramin
  if args.ramax is not None:
    mask &= df[dec_col] < args.ramax
  if args.decmin is not None:
    mask &= df[dec_col] > args.decmin
  if args.decmax is not None:
    mask &= df[dec_col] < args.decmax
  df = df[mask]
  
  dl_crossmatch(
    table=df,
    table_cols=args.tabcols,
    catalog=args.cat,
    catalog_cols=args.catcols,
    output_path=args.output,
    join=args.join,
    radius=args.radius,
    table_ra_col=ra_col,
    table_dec_col=dec_col,
    catalog_ra_col=args.catra,
    catalog_dec_col=args.catdec,
    overwrite=args.overwrite,
    cache_dir=args.cache,
    # overwrite_cache=args.overwritecache,
    workers=args.workers,
    username=args.username,
    password=args.password,
  )
  

def handle_ls(args: Namespace):
  from pylegs.tap import print_mydb_tables
  
  print_mydb_tables(username=args.username, password=args.password)
  
  
  
  
def handle_pldrop(args: Namespace):
  from pylegs.tap import drop_mydb_pylegs

  drop_mydb_pylegs(username=args.username, password=args.password) 




def handle_drop(args: Namespace):
  from pylegs.tap import drop_mydb_table
  
  drop_mydb_table(table=args.table, username=args.username, password=args.password)



def entrypoint():
  parser = ArgumentParser(
    prog='pylegs', 
    description='Python client for accessing Legacy Survey data'
  )
  
  subparser = parser.add_subparsers(dest='subprog')
  types_map = dict(str=str, int=int, float=float)
  
  spec_paths = list(configs.CLI_FOLDER.glob('*.yaml'))
  for p in spec_paths:
    fp = p.open()
    data = yaml.safe_load(fp)
    fp.close()
    
    prog = subparser.add_parser(data['name'], help=data['help'])
    for arg in data['args']:
      flags = arg.pop('flags')
      if not isinstance(flags, list):
        flags = [flags]
      
      kw_type = dict()
      type_ = types_map.get(arg.pop('type', None))
      if type_:
        kw_type['type'] = type_
      
      prog.add_argument(*flags, **kw_type, **arg)
  
  handler_map = {
    'dlcat': handle_dlcat,
    'cutout': handle_cutout,
    'axmatch': handle_axmatch,
    'xmatch': handle_xmatch,
    'ls': handle_ls,
    'pldrop': handle_pldrop,
    'drop': handle_drop,
  }
  args = parser.parse_args()
  handler = handler_map.get(args.subprog)
  if handler:
    handler(args)
  else:
    parser.print_help()
  


if __name__ == '__main__':
  entrypoint()