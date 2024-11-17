# Add the root directory to the sys.path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


## Main code start from here..

from AppManager.DB_config import DatabaseManager
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from keras.src.utils import to_categorical
import pandas as pd
from AppManager.logger import logger

class preprocessing:
    
    pass


logger.info('test logging module.')
logger.debug('someeror')