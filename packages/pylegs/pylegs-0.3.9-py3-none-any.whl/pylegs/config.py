from pathlib import Path
from typing import Any

import pandas as pd
import requests

from pylegs.utils import SingletonMeta

__all__ = ['configs']


  
class PylegsConfigs(metaclass=SingletonMeta):
  CUTOUT_RGB_BASE_URL = 'https://www.legacysurvey.org/viewer/jpeg-cutout'
  CUTOUT_FITS_BASE_URL = 'https://www.legacysurvey.org/viewer/fits-cutout'
  TAP_SYNC_BASE_URL = 'https://datalab.noirlab.edu/tap/sync'
  TAP_ASYNC_BASE_URL = 'https://datalab.noirlab.edu/tap/async'
  HTTP_CLIENT = requests.Session()
  
  ROOT = Path(__file__).parent
  DATA_FOLDER = ROOT / 'data'
  CORRECTION_FACTOR: str | Path | pd.DataFrame = DATA_FOLDER / 'correction_factor.dat'
  CLI_FOLDER = ROOT / 'cli'
  
  DATALAB_USERNAME = None
  DATALAB_PASSWORD = None
  
  
  def __init__(self):
    self.__class__.HTTP_CLIENT.headers.update({'User-Agent': f'Pylegs v0.1'})
  
  def __getattr__(self, name: str):
    return self.__class__.__dict__.get(name)

  def __setattr__(self, name: str, value: Any) -> None:
    if name in self.__class__.__dict__.keys():
      setattr(self.__class__, name, value)
    else:
      raise ValueError(f'{name} is not a valid config key')
    
  def __repr__(self) -> str:
    r = 'Pylegs Global Settings:\n'
    for k, v in self.__class__.__dict__.items():
      if not k.startswith('_'):
        r += f'{k}: {v}\n'
    return r
  
  
configs = PylegsConfigs()