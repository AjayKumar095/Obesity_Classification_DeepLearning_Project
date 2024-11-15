# Add the root directory to the sys.path
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


## Main code start here..

from AppManager.DB_config import sample_connect

print(sample_connect(db_name='xyz_db'))