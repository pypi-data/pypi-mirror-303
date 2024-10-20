"""
High-level interface for data access using Table Access Protocol (TAP)
"""


import os
import secrets
import shutil
import tempfile
import time
from functools import wraps
from getpass import getpass
from inspect import getfullargspec
from io import BytesIO
from pathlib import Path
from typing import Callable, Dict, List, Literal, Sequence, Union
from urllib.parse import quote, urlencode

import numpy as np
import pandas as pd
import requests
from astropy import units as u
from astropy.table import Table
from astropy.units import Quantity
from bs4 import BeautifulSoup
from dl import authClient as ac
from dl import queryClient as qc

from pylegs.config import configs
from pylegs.io import (PathLike, PathOrFile, TableLike, _create_parents,
                       _prepare_path, concat_tables, download_file,
                       parallel_function_executor, read_table, write_table)
from pylegs.utils import SingletonMeta, guess_coords_columns, sanitize_quantity

__all__ = [
  'dl_crossmatch', 'sync_query', 'async_query', 'batch_sync_query', 
  'batch_async_query'
]

DEFAULT_CATALOG_COLUMNS = [
  'ra', 'dec', 'fracflux_r', 'fracin_r', 'fracmasked_r',
  'mag_g', 'mag_i', 'mag_r', 'mag_z',
  'nea_g', 'nea_i', 'nea_r', 'nea_z', 'nest4096', 'ngood_g', 'ngood_i', 
  'ngood_r', 'ngood_z', 'nobs_g', 'nobs_i', 'nobs_r', 'nobs_z', 'ring256', 
  'sersic', 'shape_e1', 'shape_e2', 'shape_r', 'snr_g', 'snr_i', 'snr_r', 
  'snr_z', 'type'
]



class DataLabAuth(metaclass=SingletonMeta):
  def __init__(self):
    self._token: str | None = None
    self._username: str | None = None
    self._password: str | None = None
  
  def login(self, username: str, password: str) -> str:
    self._username = username
    self._password = password
    return self.token
  
  @property
  def token(self) -> str:
    if self._token is None or not ac.isTokenLoggedIn(self._token):
      username = self._username or configs.DATALAB_USERNAME or os.environ.get('DATALAB_USERNAME')
      password = self._password or configs.DATALAB_PASSWORD or os.environ.get('DATALAB_PASSWORD')
      if username is None:
        username = input('\nDatalab Username: ')
      if password is None:
        password = getpass('Datalab Password: ')
      if ac.isValidUser(username):
        self._token = ac.login(username, password)
    return self._token



def dl_auth(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    username = kwargs.get('username')
    password = kwargs.get('password')
    DataLabAuth().login(username, password)
    return func(*args, **kwargs)
  return wrapper



def _dl_crossmatch(
  table: TableLike = None,
  table_cols: Sequence[str] = None,
  catalog: str = 'ls_dr10.tractor',
  catalog_cols: Sequence[str] = None,
  output_path: PathOrFile = None,
  join: Literal['left', 'right', 'outer', 'inner', 'cross'] = 'left',
  radius: float | str | Quantity = '1 arcsec',
  tab_ra: str = None,
  tab_dec: str = None,
  cat_ra: str = 'ra',
  cat_dec: str = 'dec',
):
  token = DataLabAuth().token
    
  df = read_table(table)
  tab_ra, tab_dec = guess_coords_columns(df, tab_ra, tab_dec)
  df = df[[tab_ra, tab_dec]].copy()
  df['_pylegs_key'] = range(len(df))
  df = df.rename(columns={tab_ra: 'ra', tab_dec: 'dec'})
  
  radius = sanitize_quantity(radius, u.deg, True)
  
  mydb_table_name = f'pylegs_input_{secrets.token_hex(4)}'
  qc.mydb_import(token, mydb_table_name, df)
  
  sql_template = """
    SELECT local._pylegs_key, {remote_columns},
    (q3c_dist(local.ra, local.dec, remote.{cat_ra}, remote.{cat_dec})*3600.0) as dist_arcsec 
    FROM mydb://{mydb_table_name} AS local 
    INNER JOIN LATERAL (
      SELECT cat.* FROM {catalog} AS cat
      WHERE q3c_join(local.ra, local.dec, cat.{cat_ra}, cat.{cat_dec}, {sep_deg}) 
      ORDER BY q3c_dist(local.ra, local.dec, cat.{cat_ra}, cat.{cat_dec}) ASC LIMIT 1
    ) as remote ON true
  """
  sql = sql_template.format(
    remote_columns=', '.join([f'remote.{c}' for c in catalog_cols]),
    mydb_table_name=mydb_table_name,
    catalog=catalog,
    sep_deg=radius.value,
    cat_ra=cat_ra,
    cat_dec=cat_dec,
  )

  match_df = qc.query(
    token=token,
    sql=sql,
    fmt='pandas',
    out=None,
    drop=True,
    async_=False,
    timeout=600,
  )
  
  qc.mydb_drop(mydb_table_name, token=token)
  
  df = read_table(table, columns=table_cols)
  df['_pylegs_key'] = range(len(df))
  result_df = df.set_index('_pylegs_key').join(
    match_df.set_index('_pylegs_key'), how=join
  )
  
  if output_path is not None:
    write_table(result_df, output_path)
  
  return result_df



@dl_auth
def dl_crossmatch(
  table: TableLike = None,
  table_cols: Sequence[str] = None,
  catalog: str = 'ls_dr10.tractor',
  catalog_cols: Sequence[str] = None,
  output_path: PathOrFile = None,
  join: Literal['left', 'inner'] = 'inner',
  radius: float | str | Quantity = '1 arcsec',
  tab_ra: str = None,
  tab_dec: str = None,
  cat_ra: str = 'ra',
  cat_dec: str = 'dec',
  cache_dir: PathLike | None = None,
  workers: int = 5,
  overwrite: bool = False,
  **kwargs
):
  if output_path and isinstance(output_path, PathLike):
    output_path = Path(output_path)
    if output_path.exists() and not overwrite:
      return

  chunk_rows = 100_000
  df = read_table(table)
  n_splits = int(np.ceil(len(df) / chunk_rows))
  
  func_args = {
    'table': table,
    'table_cols': table_cols,
    'catalog': catalog,
    'catalog_cols': catalog_cols,
    'output_path': output_path,
    'join': join,
    'radius': radius,
    'tab_ra': tab_ra,
    'tab_dec': tab_dec,
    'cat_ra': cat_ra,
    'cat_dec': cat_dec,
  }
  
  if n_splits < 2:
    return _dl_crossmatch(**func_args)
  else:
    if cache_dir is None:
      cache_dir = Path(tempfile.gettempdir()) / f'pylegs_xmatch_{secrets.token_hex(4)}'
      cache_dir.mkdir(parents=True, exist_ok=True)
    else:
      cache_dir = Path(cache_dir)
      cache_dir.mkdir(parents=True, exist_ok=True)
    
    params = [
      {
        **func_args, 
        'table': df.iloc[i*chunk_rows : (i+1)*chunk_rows].copy(),
        'output_path': cache_dir / f'{i}.parquet'
      } 
      for i in range(n_splits)
    ]
    
    parallel_function_executor(
      func=_dl_crossmatch,
      params=params,
      workers=workers,
      progress=True,
      ignore_error=False,
      unit='query',
    )
    
    df = concat_tables(sorted([str(p.absolute()) for p in cache_dir.glob('*')]))
    shutil.rmtree(cache_dir)
    
    if output_path:
      write_table(df, output_path)
        
    return df



@dl_auth
def print_mydb_tables(**kwargs):
  token = DataLabAuth().token
  ls = qc.list(token, '')
  print(ls)



@dl_auth
def drop_mydb_pylegs(**kwargs):
  token = DataLabAuth().token
  tables = qc.list(token, '')
  tables = tables.split('\n')
  for t in tables:
    if t.startswith('pylegs'):
      qc.mydb_drop(token, t)


@dl_auth
def drop_mydb_table(table: str, **kwargs):
  token = DataLabAuth().token
  qc.mydb_drop(token, table)



def sync_query(
  query: str, 
  save_path: PathOrFile = None,
  overwrite: bool = True,
  http_client: requests.Session = configs.HTTP_CLIENT,
  dtype: Literal['bytes', 'pandas', 'astropy'] = 'bytes'
) -> bytes | pd.DataFrame | Table:
  params = {
    'request': 'doQuery',
    'version': 1.0,
    'lang': 'ADQL',
    'phase': 'run',
    'format': 'csv',
    'query': query
  }
  save_path = _prepare_path(save_path)
  _create_parents(save_path)
  
  # req_url = configs.TAP_SYNC_BASE_URL + '?' + urlencode(params)
  table_bytes = None
  attempt = 0
  max_attempts = 5
  while table_bytes is None and attempt < max_attempts:
    table_bytes = download_file(
      url=configs.TAP_SYNC_BASE_URL,#req_url, 
      save_path=save_path, 
      overwrite=overwrite,
      query=params,
      http_client=http_client,
    )
    attempt += 1
  
  if dtype == 'bytes':
    return table_bytes
  if dtype in ('pandas', 'astropy'):
    return read_table(BytesIO(table_bytes), fmt='csv', dtype=dtype)


def async_query(
  query: str, 
  save_path: PathOrFile = None,
  overwrite: bool = True,
  http_client: requests.Session = configs.HTTP_CLIENT,
  delay: int = 5,
  dtype: Literal['bytes', 'pandas', 'astropy'] = 'bytes'
) -> bytes | pd.DataFrame | Table:
  params = {
    'request': 'doQuery',
    'version': 1.0,
    'lang': 'ADQL',
    'phase': 'run',
    'format': 'csv',
    'query': query
  }
  save_path = _prepare_path(save_path)
  _create_parents(save_path)
  
  table_bytes = None
  attempt = 0
  max_attempts = 5
  
  while table_bytes is None and attempt < max_attempts:
    resp = http_client.post(
      url=configs.TAP_ASYNC_BASE_URL,
      data=params,
    )
    soup = BeautifulSoup(resp.text, 'xml')
    
    job_id = soup.find('uws:jobId').text
    job_phase = soup.find('uws:phase').text
    table_bytes = None
    
    while job_phase == 'PENDING':
      time.sleep(delay)
      resp = http_client.get(configs.TAP_ASYNC_BASE_URL + f'/{job_id}')
      soup = BeautifulSoup(resp.text, 'xml')
      job_phase = soup.find('uws:phase').text
    
    if job_phase == 'COMPLETED':
      table_url = soup.find('#result').attrs['xlink:href']
      table_bytes = download_file(
        url=table_url, 
        save_path=save_path, 
        overwrite=overwrite, 
        http_client=http_client
      )
    attempt += 1
  
  if dtype == 'bytes':
    return table_bytes
  if dtype in ('pandas', 'astropy'):
    return read_table(BytesIO(table_bytes), fmt='csv', dtype=dtype)
  
  
def _batch_query(
  func: Callable,
  queries: Sequence[str],
  save_paths: Sequence[str | Path],
  func_args: Dict[str, None],
  workers: int = 3,
  concat: bool = False,
  partial_paths: Sequence[str | Path] | None = None,
):
  save_paths_aux = save_paths
  if concat:
    if partial_paths is None:
      tmp_folder = Path(tempfile.gettempdir()) / f'pylegs_tap_{secrets.token_hex(4)}'
      tmp_folder.mkdir(parents=True, exist_ok=True)
      save_paths_aux = [tmp_folder / f'{i}.csv' for i in range(len(queries))]
    else:
      save_paths_aux = [Path(i) for i in partial_paths]
      save_paths_aux[0].parent.mkdir(parents=True, exist_ok=True)
    
  params = [
    {
      'query': _query,
      'save_path': _save_path,
      **func_args,
    }
    for _query, _save_path in zip(queries, save_paths_aux)
  ]
  
  try:
    parallel_function_executor(
      func,
      params=params,
      workers=workers,
      unit='query',
      ignore_error=False,
    )

    if concat:
      combined_df = concat_tables([p for p in save_paths_aux if p.exists()])
      write_table(combined_df, save_paths)
      if partial_paths is None:
        shutil.rmtree(tmp_folder)
  except Exception as e:
    if concat and partial_paths is None:
      shutil.rmtree(tmp_folder)
    raise e


def batch_sync_query(
  queries: str, 
  save_paths: PathOrFile = None,
  overwrite: bool = True,
  concat: bool = False,
  workers: int = 3,
  http_client: requests.Session = configs.HTTP_CLIENT,
  partial_paths: Sequence[str | Path] | None = None,
  overwrite_partials: bool = False,
) -> bytes | pd.DataFrame | Table:
  args = {
    'overwrite': overwrite_partials if concat else overwrite,
    'http_client': http_client,
  }
  _batch_query(
    func=sync_query, 
    queries=queries, 
    save_paths=save_paths, 
    func_args=args, 
    workers=workers, 
    concat=concat,
    partial_paths=partial_paths,
  )
  
  
def batch_async_query(
  queries: str, 
  save_paths: PathOrFile = None,
  overwrite: bool = True,
  concat: bool = False,
  workers: int = 3,
  http_client: requests.Session = configs.HTTP_CLIENT,
  delay: int = 5,
  partial_paths: Sequence[str | Path] | None = None,
  overwrite_partials: bool = False,
) -> bytes | pd.DataFrame | Table:
  args = {
    'overwrite': overwrite,
    'http_client': http_client,
    'delay': delay,
  }
  _batch_query(
    func=async_query, 
    queries=queries, 
    save_paths=save_paths, 
    func_args=args, 
    workers=workers, 
    concat=concat,
    partial_paths=partial_paths,
  )



def download_catalog(
  save_path: PathOrFile,
  columns: Sequence[str] | None = None,
  ra_min: float | Quantity = 0,
  ra_max: float | Quantity = 360,
  delta_ra: float | Quantity = 10 * u.arcmin,
  table: str = 'ls_dr10.tractor',
  exclude_types: Sequence[str] | None = ['PSF'],
  magr_min: float | None = None,
  magr_max: float | None = None,
  dec_min: float | Quantity = -90,
  dec_max: float | Quantity = 90, 
  brick_primary: bool | None = True,
  overwrite: bool = False,
  workers: int = 6,
  tmp_folder: str | Path | None = None,
  overwrite_tmp: bool = False,
):
  """
  PSF, REX, DEV, EXP, SER, DUP
  """
  if columns is None:
    columns = DEFAULT_CATALOG_COLUMNS
    
  filters = ''
  if magr_min is not None and magr_max is not None:
    filters += f'AND mag_r BETWEEN {magr_min:.7f} AND {magr_max:.7f} '
  if brick_primary:
    filters += f'AND brick_primary = 1 '
  if exclude_types is not None:
    for t in exclude_types:
      filters += f"AND type != '{t.upper()}' "
  
  template = """
  SELECT {cols}
  FROM {table}
  WHERE ra BETWEEN {ra_min:.12f} AND {ra_max:.12f}
  AND dec BETWEEN {dec_min:.8f} AND {dec_max:.8f}
  {filters}
  """.strip()
  
  print('Summary:')
  ra_min = sanitize_quantity(ra_min, u.deg, convert=True)
  ra_max = sanitize_quantity(ra_max, u.deg, convert=True)
  print(f'RA range: [{ra_min}, {ra_max}]')
  ra_min, ra_max = ra_min.value, ra_max.value
  
  dec_min = sanitize_quantity(dec_min, u.deg, convert=True)
  dec_max = sanitize_quantity(dec_max, u.deg, convert=True)
  print(f'DEC range: [{dec_min}, {dec_max}]')
  dec_min, dec_max = dec_min.value, dec_max.value

  delta_ra = sanitize_quantity(delta_ra, u.deg, convert=True)
  print(f'RA step: {delta_ra}')
  delta_ra = delta_ra.value
  
  queries = [
    template.format(
      cols=', '.join(columns), 
      table=table, 
      magr_min=magr_min, 
      magr_max=magr_max, 
      filters=filters,
      dec_min=dec_min,
      dec_max=dec_max,
      ra_min=_ra_min,
      ra_max=_ra_min + delta_ra,
    )
    for _ra_min in np.arange(ra_min, ra_max, delta_ra)
  ]
  
  tmp_paths = None
  if tmp_folder is not None:
    tmp_paths = [
      Path(tmp_folder) / f'query_{_ra:.6f}-{(_ra+delta_ra):.6f}.csv' 
      for _ra in np.arange(ra_min, ra_max, delta_ra)
    ]
  
  print('\nExample query:')
  print(queries[0])
  print(f'\nNumber of queries: {len(queries)}\n')
  
  return batch_sync_query(
    queries=queries, 
    save_paths=save_path, 
    overwrite=overwrite, 
    concat=True, 
    workers=workers,
    partial_paths=tmp_paths,
    overwrite_partials=overwrite_tmp,
  )




if __name__ == '__main__':
  # sync_query(
  #   'select top 10 psfdepth_g, psfdepth_r from ls_dr9.tractor where ra between 230.2939-0.0013 and 230.2939+0.0013 and dec between 29.7714-0.0013 and 29.7714+0.0013',
  #   url='https://datalab.noirlab.edu/tap/sync'
  # )
  # sync_query('select top 10 psfdepth_g, psfdepth_r from ls_dr9.tractor where ra between 230.2939-0.0013 and 230.2939+0.0013 and dec between 29.7714-0.0013 and 29.7714+0.0013')
  download_catalog(ra_min=120, ra_max=120*u.deg+2*u.arcmin, save_path='test.parquet', delta_ra=1*u.arcmin, magr_min=15, magr_max=16, overwrite=True)