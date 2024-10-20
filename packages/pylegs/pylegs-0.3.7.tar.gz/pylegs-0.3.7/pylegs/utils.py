import re
from datetime import datetime, timedelta
from multiprocessing import Lock
from pathlib import Path
from typing import Sequence, Tuple

import numpy as np
import pandas as pd
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.units import Quantity, Unit

RA_REGEX = re.compile(r'^ra_?J?\d*$', re.IGNORECASE)
DEC_REGEX = re.compile(r'^dec_?J?\d*$', re.IGNORECASE)




def _match_regex_against_sequence(
  regex: re.Pattern, 
  columns: Sequence[str]
) -> Tuple[int, str] | None:
  for i, col in enumerate(columns):
    if regex.match(col):
      return i, col
  return None

  
def guess_coords_columns(
  df: pd.DataFrame,
  ra: str | None = None,
  dec: str | None = None,
) -> Tuple[str, str]:
  """
  Receives a pandas dataframe and try to guess the columns names used to
  identify the RA and DEC coordinates.

  Parameters
  ----------
  df : pd.DataFrame
    A pandas dataframe
  ra : str | None, optional
    The column name used to name the RA column. If a string is passed, this
    function will skip the RA guessing and will return the value of RA passed
    by this parameter. If the value is set to ``None``, this function will
    guess the RA column name using a pre-defined regular expression and will
    return the value of the first match found following the sequence of
    the columns.
  dec : str | None, optional
    The column name used to name the DEC column. If a string is passed, this
    function will skip the DEC guessing and will return the value of DEC passed
    by this parameter. If the value is set to ``None``, this function will
    guess the DEC column name using a pre-defined regular expression and will
    return the value of the first match found following the sequence of
    the columns.

  Returns
  -------
  Tuple[str, str]
    A tuple of RA and DEC columns guessed.

  Raises
  ------
  ValueError
    Raises a error if the RA or DEC columns cannot be found.
  """
  cols = df.columns.to_list()
  if ra is None:
    _, ra = _match_regex_against_sequence(RA_REGEX, cols)
  if dec is None:
    _, dec = _match_regex_against_sequence(DEC_REGEX, cols)
  if ra is None or dec is None:
    raise ValueError(
      "Can't guess RA or DEC columns, please, specify the columns names "
      "via `ra` and `dec` parameters"
    )
  return ra, dec


def iauname(
  ra: float | np.ndarray,
  dec: float | np.ndarray
) -> str | Sequence[str]:
  """
  Receives the angular position(s) of the object(s) and returns IAU2000 name(s)

  Parameters
  ----------
  ra: float or array of float
    The right ascension of the object(s).
  dec: float or array of float
    The declination of the object(s).

  Example
  --------
  >>> iauname(187.70592, 12.39112)
  'J123049.42+122328.03'

  Returns
  -------
  str or list of str
    The formated IAU name of the object(s)
  """
  coord = SkyCoord(ra=ra*u.degree, dec=dec*u.degree, frame='icrs')
  ra_str = coord.ra.to_string(unit=u.hourangle, sep='', precision=2, pad=True)
  dec_str = coord.dec.to_string(sep='', precision=1, alwayssign=True, pad=True)
  if isinstance(ra_str, np.ndarray):
    r = [f'J{_ra_str}{_dec_str}' for _ra_str, _dec_str in zip(ra_str, dec_str)]
  else:
    r = f'J{ra_str}{dec_str}'
  return r



def iauname_path(
  iaunames: str | Sequence[str] = None,
  ra: float | Sequence[float] = None,
  dec: float | Sequence[float] = None,
  prefix: str | Path = '',
  suffix: str = '',
  flat: bool = False,
  return_str: bool = False,
) -> Path | Sequence[Path]:
  """
  Calculate the nested path for a given iauname

  Parameters
  ----------
  iaunames: str, List[str], optional
    Object iauname. The iauname or RA and DEC must be passed, if ``iaunames`` is
    ``None``, this function computes the iauname using the ``ra`` and ``dec``
    parameters
  ra: float, List[float], optional
    Object RA, used only if ``iaunames`` is ``None``
  dec: float, List[float], optional
    Object DEC, used only if ``iaunames`` is ``None``
  prefix: str, Path, optional
    Path that will be prepended at the begin of all paths
  suffix: str, optional
    Suffix that will be appended at the end of all paths
  flat: bool, optional
    Create the flat path with all files inside a same parent folder. This is
    not recomended for big datasets
  return_str: bool, optional
    Cast all paths to string before returning

  Example
  -------
  iaunames_path('J123049.42+122328.03', '.png')
  Path('J123/J123049.42+122328.03.png')

  Returns
  -------
  Path, List[Path]
    The iauname path
  """
  if iaunames is None:
    iaunames = iauname(ra, dec)

  if flat:
    mapping = lambda x:  Path(prefix) / (x + suffix)
  else:
    mapping = lambda x: Path(prefix) / x[:4] / (x + suffix)

  prep_output = lambda x: str(x) if return_str else x

  if isinstance(iaunames, str):
    return prep_output(mapping(iaunames))
  else:
    return [prep_output(mapping(x)) for x in iaunames]
  
  
def sanitize_quantity(
  quantity: float | int | Sequence | Quantity, 
  unit: str | Unit, 
  convert: bool = False
) -> Quantity:
  if isinstance(unit, str):
    unit = Unit(unit)
  if isinstance(quantity, str):
    if convert:
      return Quantity(quantity).to(unit)
    return Quantity(quantity)
  if isinstance(quantity, Quantity):
    if convert:
      return quantity.to(unit)
    return quantity
  return quantity * unit


class SingletonMeta(type):
  """
  Thread-safe implementation of Singleton.
  """
  _instances = {}
  """The dict storing memoized instances"""

  _lock = Lock()
  """
  Lock object that will be used to synchronize threads during
  first access to the Singleton.
  """

  def __call__(cls, *args, **kwargs):
    """
    Possible changes to the value of the `__init__` argument do not affect
    the returned instance.
    """
    # When the program has just been launched. Since there's no
    # Singleton instance yet, multiple threads can simultaneously pass the
    # previous conditional and reach this point almost at the same time. The
    # first of them will acquire lock and will proceed further, while the
    # rest will wait here.
    with cls._lock:
      # The first thread to acquire the lock, reaches this conditional,
      # goes inside and creates the Singleton instance. Once it leaves the
      # lock block, a thread that might have been waiting for the lock
      # release may then enter this section. But since the Singleton field
      # is already initialized, the thread won't create a new object.
      if cls not in cls._instances:
        instance = super().__call__(*args, **kwargs)
        cls._instances[cls] = instance
    return cls._instances[cls]


class Timer:
  def __init__(self, start: bool = True):
    self.start_time = None
    self.end_time = None
    if start:
      self.start()

  def __repr__(self) -> str:
    return self.duration

  def start(self):
    self.start_time = datetime.now()

  def end(self) -> timedelta:
    self.end_time = datetime.now()
    return self.duration

  @property
  def duration(self) -> timedelta:
    if not self.end_time:
      end_time = datetime.now()
      duration = end_time - self.start_time
    else:
      duration = self.end_time - self.start_time
    return duration
  
  @property
  def duration_str(self) -> str:
    return self._format_time(self.duration)
  
  def __str__(self):
    return self.duration_str

  def _format_time(self, dt: timedelta) -> str:
    hours, remainder = divmod(dt.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))