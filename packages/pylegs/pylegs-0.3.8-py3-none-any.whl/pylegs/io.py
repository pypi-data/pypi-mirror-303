import bz2
import concurrent.futures
import re
from io import BufferedIOBase, BytesIO, RawIOBase, StringIO, TextIOBase
from pathlib import Path
from typing import Any, Callable, Dict, Literal, Sequence, Tuple

import pandas as pd
import requests
from astropy.io import fits, votable
from astropy.table import Table
from tqdm import tqdm

__all__ = [
  'download_file', 'parallel_function_executor', 'compress_fits_image',
  'read_table', 'write_table'
]


PathLike = str | Path
FileLike = BytesIO
PathOrFile = PathLike | FileLike
TableLike = pd.DataFrame | Table


def _prepare_path(path: PathOrFile) -> PathOrFile:
  if isinstance(path, str):
    return Path(path)
  return path


def _path_exists(path: PathOrFile) -> bool:
  if isinstance(path, Path):
    return path.exists()
  if isinstance(path, str):
    return Path(path).exists()
  return False


def _create_parents(path: PathOrFile):
  if isinstance(path, (str, Path)):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    
    
def _write_bytes(path: PathOrFile, b: bytes):
  if isinstance(path, (str, Path)):
    with open(path, 'wb') as f:
      f.write(b)
  if isinstance(path, BytesIO):
    path.write(b)
    
    
def _is_folder(path: PathOrFile) -> bool:
  if isinstance(path, (str, Path)):
    return Path(path).is_dir()
  return False


def download_file(
  url: str,
  save_path: PathOrFile = None,
  query: Dict[str, Any] = None,
  overwrite: bool = False,
  http_client: requests.Session = None,
  extract: bool = False,
) -> bytes | None:
  """
  Download a file from a URL and save it to a specified path.

  Parameters
  ----------
  url : str
    The URL from which to download the file.
  save_path : PathOrFile
    The path where the downloaded file will be saved. This can be a string or 
    a `pathlib.Path` object.
  query : Dict[str, Any], optional
    A dictionary of query parameters to include in the request. Defaults to ``None``.
  overwrite : bool, optional
    If True, overwrite the existing file at `save_path`. Defaults to ``False``.
  http_client : requests.Session, optional
    The HTTP client to use for making the request. If None, the `requests` 
    library is used. Defaults to ``None``.
  extract : bool, optional
    If ``True``, decompress the downloaded file if it is in ``bz2`` format. 
    Defaults to ``False``.

  Returns
  -------
  bytes or None
    The bytes of the downloaded (and possibly decompressed) file, or None if 
    the file already exists and `overwrite` is False.

  Notes
  -----
  - If ``overwrite`` is ``False`` and the file already exists at ``save_path``, 
    the function returns ``None`` without downloading the file.
  - If ``extract`` is ``True``, the function assumes the file is compressed 
    with bz2 and decompresses it before saving.

  Raises
  ------
  Exception
    If the HTTP request fails or if there is an error in writing the file.

  Examples
  --------
  >>> download_file('http://example.com/file.txt', 'file.txt')
  b'file content'
  
  >>> download_file('http://example.com/file.bz2', 'file.txt', extract=True)
  b'decompressed content'
  """
  save_path = _prepare_path(save_path)

  if _path_exists(save_path) and not overwrite:
    return None

  _create_parents(save_path)

  http_client = http_client or requests

  r = http_client.get(url, params=query, allow_redirects=True)

  file_bytes = None
  if r.status_code == 200:
    if extract:
      file_bytes = bz2.decompress(r.content)
    else:
      file_bytes = r.content
    
    if save_path is not None:
      _write_bytes(save_path, file_bytes)

  return file_bytes


def compress_fits_image(
  file: PathOrFile,
  save_path: str | Path = None,
  overwrite: bool = True,
  compress_type: Literal['RICE_1', 'RICE_ONE', 'PLIO_1', 'GZIP_1', 'GZIP_2', 'HCOMPRESS_1', 'NOCOMPRESS'] = 'NOCOMPRESS',
  hcomp_scale: int = 3,
  quantize_level: int = 10,
  quantize_method: Literal[-1, 1, 2] = -1,
  tile_shape: Tuple[int, int] = None,
  dither_seed: int = 0,
  ext: int = 0,
):
  """
  Compress a FITS image and optionally save the compressed image to a file.

  Parameters
  ----------
  file : PathOrFile
    The path to the FITS file to be compressed. This can be a string or a 
    `pathlib.Path` object.
  save_path : str or Path, optional
    The path where the compressed FITS image will be saved. If None, 
    the compressed image is not saved.
    Defaults to None.
  overwrite : bool, optional
    If ``True``, overwrite the existing file at ``save_path``. Defaults to ``True``.
  compress_type : str, optional
    The compression algorithm to use. Supported values include 
    ``'HCOMPRESS_1'``, ``'RICE_1'``, ``'GZIP_1'``, ``'PLIO_1'``.
    Defaults to 'HCOMPRESS_1'.
  hcomp_scale : int, optional
    The scale parameter for HCOMPRESS. Defaults to 3.
  quantize_level : int, optional
    The quantization level for compression. Defaults to 10.
  quantize_method : int, optional
    The quantization method to use. Defaults to -1.
  ext : int, optional
    The ``ext`` of the FITS file to compress. Defaults to 0.
  random_seed : int, optional
    The seed for random number generation used in dithering. Defaults to 42.

  Returns
  -------
  fits.CompImageHDU
    The compressed image HDU.

  Raises
  ------
  ValueError
    If the specified FITS ``ext`` is out of range.
  
  Notes
  -----
  If ``save_path`` is provided and ``overwrite`` is True, the compressed 
  image will be saved to the specified path. Otherwise, the function returns 
  the compressed image HDU.

  Examples
  --------
  >>> compress_fits_image('input.fits', save_path='compressed.fits', compress_type='RICE_1')
  <astropy.io.fits.hdu.compressed.CompImageHDU object at 0x...>
  """
  hdul = fits.open(file)

  if ext >= len(hdul):
    raise ValueError(f'Trying to access ext {ext}, max ext is {len(hdul)-1}')

  if _path_exists(save_path) and not overwrite:
    return None

  comp = None
  comp = fits.CompImageHDU(
    data=hdul[ext].data,
    header=hdul[ext].header,
    compression_type=compress_type,
    hcomp_scale=hcomp_scale,
    quantize_level=quantize_level,
    quantize_method=quantize_method,
    tile_shape=tile_shape,
    dither_seed=dither_seed,
  )
  if save_path:
    comp.writeto(save_path, overwrite=overwrite)
  
  return comp


def read_table(
  path: TableLike | PathOrFile,
  fmt: str | None = None,
  columns: Sequence[str] | None = None,
  low_memory: bool = False,
  comment: str | None = None,
  na_values: Sequence[str] | Dict[str, Sequence[str]] = None,
  keep_default_na: bool = True,
  na_filter: bool = True,
  header: Literal['infer'] | int | Sequence[int] = 'infer',
  col_names: Sequence[str] | None = None,
  dtype: Literal['pandas', 'astropy'] = 'pandas',
) -> pd.DataFrame:
  """
  This function tries to detect the table type comparing the file extension and
  returns a pandas dataframe of the loaded table.
  
  Supported table types:
  
    =============== ===========================
    Table Type      Extensions
    =============== ===========================
    Fits            .fit, .fits, .fz
    Votable         .vo, .vot, .votable, .xml
    ASCII           .csv, .tsv, .dat
    Heasarc         .tdat
    Arrow           .parquet, .feather
    =============== ===========================

  Parameters
  ----------
  path : str or Path
    Path to the table to be read.
  
  fmt : str or None
    Specify the file format manually to avoid inference by file extension. This
    parameter can be used to force a specific parser for the given file.
  
  columns : sequence of str or None
    If specified, only the column names in list will be loaded. Can be used to
    reduce memory usage.
  
  low_memory : bool
    Internally process the file in chunks, resulting in lower memory use while 
    parsing, but possibly mixed type inference. To ensure no mixed types either 
    set False, or specify the type with the dtype parameter. Note that the 
    entire file is read into a single DataFrame regardless, use the chunksize 
    or iterator parameter to return the data in chunks. (Only valid with C parser).
    
    .. note::
      Used only for ASCII tables, ignored by other types of tables.
  
  comment : str or None
    Character indicating that the remainder of line should not be parsed. 
    If found at the beginning of a line, the line will be ignored altogether. 
    This parameter must be a single character. Like empty lines 
    (as long as ``skip_blank_lines=True``), fully commented lines are ignored 
    by the parameter header but not by skiprows. For example, if ``comment='#'``, 
    parsing ``#empty\\na,b,c\\n1,2,3`` with ``header=0`` will result in 
    ``'a,b,c'`` being treated as the header.
    
    .. note::
      Used only for ASCII tables, ignored by other types of tables.
  
  na_values: hashable, iterable of hashable or dict of `HashableIterable`
    Additional strings to recognize as ``NA``/``NaN``. If ``dict`` passed, specific 
    per-column ``NA`` values. By default the following values are interpreted 
    as `NaN`: “ “, “#N/A”, “#N/A N/A”, “#NA”, “-1.#IND”, “-1.#QNAN”, “-NaN”, 
    “-nan”, “1.#IND”, “1.#QNAN”, “<NA>”, “N/A”, “NA”, “NULL”, “NaN”, “None”, 
    “n/a”, “nan”, “null “.
    
    .. note::
      Used only for ASCII tables, ignored by other types of tables.
  
  keep_default_na : bool 
    Whether or not to include the default ``NaN`` values when parsing the data. 
    Depending on whether ``na_values`` is passed in, the behavior is as follows:

    - If ``keep_default_na`` is ``True``, and ``na_values`` are specified, 
      `na_values` is appended to the default NaN values used for parsing.
    - If ``keep_default_na`` is ``True``, and ``na_values`` are not specified, only the 
      default ``NaN`` values are used for parsing.
    - If ``keep_default_na`` is ``False``, and ``na_values`` are specified, only 
      the ``NaN`` values specified na_values are used for parsing.
    - If ``keep_default_na`` is ``False``, and ``na_values`` are not specified, 
      no strings will be parsed as ``NaN``.

    Note that if ``na_filter`` is passed in as ``False``, the ``keep_default_na`` and 
    ``na_values`` parameters will be ignored.
    
    .. note::
      Used only for ASCII tables, ignored by other types of tables.
  
  na_filter : bool
    Detect missing value markers (empty strings and the value of ``na_values``). 
    In data without any ``NA`` values, passing ``na_filter=False`` can improve the 
    performance of reading a large file.
    
    .. note::
      Used only for ASCII tables, ignored by other types of tables.
      
  header : 'infer' or int or sequence of int
    Row number(s) containing column labels and marking the start of the data 
    (zero-indexed). Default behavior is to infer the column names: if no ``names``
    are passed the behavior is identical to ``header=0`` and column names are 
    inferred from the first line of the file, if column names are passed 
    explicitly to ``names`` then the behavior is identical to ``header=None``. 
    Explicitly pass ``header=0`` to be able to replace existing names. The 
    header can be a list of integers that specify row locations for a 
    `pandas.MultiIndex` on the columns e.g. ``[0, 1, 3]``. Intervening rows 
    that are not specified will be skipped (e.g. 2 in this example is skipped). 
    Note that this parameter ignores commented lines and empty lines if 
    ``skip_blank_lines=True``, so ``header=0`` denotes the first line of data 
    rather than the first line of the file.
    
    .. note::
      Used only for ASCII tables, ignored by other types of tables.
    
  col_names : sequence of str
    Sequence of column labels to apply. If the file contains a header row, 
    then you should explicitly pass ``header=0`` to override the column names. 
    Duplicates in this list are not allowed.
    
    .. note::
      Used only for ASCII tables, ignored by other types of tables.
      
  dtype : 'pandas' or 'astropy'
    The data type returned by this function. 
    
    - If ``'pandas'`` (default) is specified, the table will be loaded as a 
      pandas dataframe
    - If ``'astropy'`` is specified, the table will be loaded as a astropy table

  Notes
  -----
  The Transportable Database Aggregate Table (TDAT) type is a data structure 
  created by NASA's Heasarc project and a very simple parser was implemented
  in this function due to lack of support in packages like pandas and astropy. 
  For more information, see [#TDAT]_

  Returns
  -------
  pd.DataFrame
    The table as a pandas dataframe

  Raises
  ------
  ValueError
    Raises an error if the file extension can not be detected
    
  References
  ----------
  .. [#TDAT] Transportable Database Aggregate Table (TDAT) Format.
      `<https://heasarc.gsfc.nasa.gov/docs/software/dbdocs/tdat.html>`_
  """
  is_file_like = False
  if isinstance(path, str):
    if path.startswith('http://') or path.startswith('https://') or path.startswith('ftp://'):
      fmt = fmt or path.split('.')[-1]
    else:
      path = Path(path)
      fmt = fmt or path.suffix
  if isinstance(path, Path):
    path = Path(path)
    fmt = fmt or path.suffix
  elif isinstance(path, pd.DataFrame):
    if columns is None:
      return path
    else:
      return path[columns].copy()
  elif isinstance(path, Table):
    df = path.to_pandas()
    if columns:
      df = df[columns]
    return df
  elif isinstance(path, (RawIOBase, BufferedIOBase, TextIOBase)):
    is_file_like = True
  
  if fmt.startswith('.'):
    fmt = fmt[1:]

  if fmt in ('fit', 'fits', 'fz'):
    with fits.open(path) as hdul:
      table_data = hdul[1].data
      table = Table(data=table_data)
      if columns is None:
        columns = [name for name in table.colnames if len(table[name].shape) <= 1]
      table = table[columns]
    if dtype == 'astropy':
      return table
    if dtype == 'pandas':
      return table.to_pandas()
  elif fmt in ('dat', 'tsv'):
    optional_params = {}
    if col_names:
      optional_params = {'names': col_names}
    df = pd.read_csv(
      path, 
      sep=r'\s+',
      usecols=columns, 
      low_memory=low_memory,
      comment=comment,
      na_values=na_values,
      keep_default_na=keep_default_na,
      na_filter=na_filter,
      header=header,
      **optional_params,
    )
    if dtype == 'pandas':
      return df
    if dtype == 'astropy':
      return Table.from_pandas(df)
  elif fmt == 'csv':
    optional_params = {}
    if col_names:
      optional_params = {'names': col_names}
    df = pd.read_csv(
      path, 
      usecols=columns, 
      low_memory=low_memory,
      comment=comment,
      na_values=na_values,
      keep_default_na=keep_default_na,
      na_filter=na_filter,
      header=header,
      **optional_params,
    )
    if dtype == 'pandas':
      return df
    if dtype == 'astropy':
      return Table.from_pandas(df)
  elif fmt == 'parquet':
    df = pd.read_parquet(
      path, 
      columns=columns,
    )
    if dtype == 'pandas':
      return df
    if dtype == 'astropy':
      return Table.from_pandas(df)
  elif fmt == 'feather':
    df = pd.read_feather(
      path, 
      columns=columns,
    )
    if dtype == 'pandas':
      return df
    if dtype == 'astropy':
      return Table.from_pandas(df)
  elif fmt == 'tdat':
    if is_file_like: raise ValueError('Not implemented for file-like objects')
    path = Path(path)
    content = path.read_text()
    header = re.findall(r'line\[1\] = (.*)', content)[0].replace(' ', '|')
    data = content.split('<DATA>\n')[-1].split('<END>')[0].replace('|\n', '\n')
    tb = header + '\n' + data
    df = pd.read_csv(
      StringIO(tb), 
      sep='|', 
      usecols=columns, 
      low_memory=low_memory
    )
    if dtype == 'pandas':
      return df
    if dtype == 'astropy':
      return Table.from_pandas(df)
  elif fmt in ('vo', 'vot', 'votable', 'xml'):
    result = votable.parse_single_table(path)
    table = result.to_table(use_names_over_ids=True)
    # table = result.get_first_table().to_table(use_names_over_ids=True)
    if columns:
      table = table[columns]
    if dtype == 'astropy':
      return table
    if dtype == 'pandas':
      return table.to_pandas

  raise ValueError(
    'Can not infer the load function for this table based on suffix. '
    'Please, use a specific loader.'
  )


def write_table(data: TableLike, path: PathOrFile, fmt: str | None = None):
  """
  Write a table to a file in various formats.

  Parameters
  ----------
  data : TableLike
    The table data to write. This can be an `astropy.table.Table` or a `pandas.DataFrame`.
  path : PathOrFile
    The path or file where the table will be written. This can be a string or a `pathlib.Path` object.
  fmt : str, optional
    The format in which to write the table. If not provided, the format is inferred from the file extension.

  Notes
  -----
  The function supports multiple output formats based on the file extension 
  or the ``fmt`` parameter:
  
  - ``'fits'``, ``'fit'``: writes to a FITS file.
  - ``'csv'``: writes to a CSV file.
  - ``'parquet'``: writes to a Parquet file.
  - ``'dat'``: writes to a space-separated text file.
  - ``'tsv'``: writes to a tab-separated text file.
  - ``'html'``: writes to an HTML file.
  - ``'feather'``: writes to a Feather file.
  - ``'vo'``, ``'vot'``, ``'votable'``, ``'xml'``: writes to a VOTable XML file.

  Raises
  ------
  ValueError
    If the provided format is not supported.

  Examples
  --------
  >>> from astropy.table import Table
  >>> import pandas as pd
  >>> data = Table({'col1': [1, 2], 'col2': [3, 4]})
  >>> write_table(data, 'output.fits')
  >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
  >>> write_table(df, 'output.csv')
  """
  if isinstance(path, str):
    fmt = fmt or Path(path).suffix
    Path(path).parent.mkdir(parents=True, exist_ok=True)
  elif isinstance(path, Path):
    fmt = fmt or path.suffix
    path.parent.mkdir(parents=True, exist_ok=True)
    path = str(path.absolute())
  
  if isinstance(data, Table):
    data = data.to_pandas()
  
  if fmt.startswith('.'):
    fmt = fmt[1:]
  
  if fmt in ('fit', 'fits'):
    Table.from_pandas(data).write(path, overwrite=True, format='fits')
  elif fmt == 'csv':
    data.to_csv(path, index=False)
  elif fmt == 'parquet':
    data.to_parquet(path, index=False)
  elif fmt == 'dat':
    data.to_csv(path, index=False, sep=' ')
  elif fmt == 'tsv':
    data.to_csv(path, index=False, sep='\t')
  elif fmt == 'html':
    data.to_html(path, index=False)
  elif fmt == 'feather':
    data.to_feather(path, index=False)
  elif fmt in ('vo', 'vot', 'votable', 'xml'):
    t = Table.from_pandas(data)
    votable.writeto(t, path)


def concat_tables(
  tables: Sequence[TableLike | PathOrFile],
  **kwargs
) -> pd.DataFrame:
  """
  Concatenate tables into a single one. This function concatenate over the
  table rows and is usefull to concatenate tables with same columns, although 
  there is no error in concatenating tables with non-existent columns in other.
  If a table does not have a certain column, the values will be filled with 
  ``NaN`` values. This function does not attempt to apply any type of 
  duplicate row removal.

  Parameters
  ----------
  tables : Sequence[TableLike  |  PathOrFile]
    A sequence of tables to be concatenated. This parameter accepts a
    table-like object (pandas dataframe, astropy table), a path to a file
    represented as a string or pathlib.Path object, or a file object
    (BinaryIO, StringIO, file-descriptor, etc).
  kwargs : Any
    Arguments that will be passed to `~astromodule.io.read_table` function

  Returns
  -------
  pd.DataFrame
    A dataframe of the concatenated table
  """
  dfs = [read_table(df, **kwargs) for df in tables]
  dfs = [df for df in dfs if isinstance(df, pd.DataFrame) and not df.empty]
  if len(dfs) > 0:
    return pd.concat(dfs)
  return pd.DataFrame()


def parallel_function_executor(
  func: Callable,
  params: Sequence[Dict[str, Any]] = [],
  workers: int = 2,
  callback: Callable = None,
  progress: bool = True,
  ignore_error: bool = True,
  unit: str = 'it'
):
  """
  Execute a function in parallel using multiple threads.

  Parameters
  ----------
  func : :term:`python:callable`
    The function to be executed in parallel.
  params : sequence of dict, optional
    A list of dictionaries containing the keyword arguments to be passed to 
    ``func`` for each call. Defaults to an empty list.
  workers : int, optional
    The number of worker threads to use. Defaults to 2.
  callback : :term:`python:callable`, optional
    A function to be called with the result of each ``func`` call. 
    Defaults to `None`.
  progress : bool, optional
    If `True`, displays a progress bar. Defaults to `True`.
  ignore_error : bool, optional
    If `True`, ignores exceptions raised by ``func`` calls. 
    Defaults to `True`.
  unit : str, optional
    The unit label to use in the progress bar. Defaults to ``'it'``.

  Raises
  ------
  Exception
    If ``ignore_error`` is `False`, raises the exception encountered during 
    the ``func`` execution.

  Notes
  -----
  The ``callback`` function will be called with the result of each successful 
  ``func`` execution. If ``ignore_error`` is False and an exception occurs 
  during the execution of ``func``, the exception will be raised and the 
  remaining tasks will not be executed.

  Examples
  --------
  >>> def func(x, y):
  ...     return x + y
  ...
  >>> params = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}]
  >>> parallel_function_executor(func, params, workers=2, callback=print)
  3
  7
  """
  with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
    if progress:
      pbar = tqdm
    else:
      pbar = lambda *args, **kwargs: args[0]
      
    callback = callback or (lambda *args, **kwargs: None)
    
    futures = []
    for i in range(len(params)):
      futures.append(executor.submit(func, **params[i]))

    for future in pbar(
      concurrent.futures.as_completed(futures),
      total=len(futures),
      unit=unit
    ):
      try:
        callback(future.result())
      except Exception as e:
        if not ignore_error:
          raise e