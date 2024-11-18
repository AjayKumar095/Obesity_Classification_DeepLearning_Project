# Add the root directory to the sys.path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

## PyTest
import pytest 
import sqlite3
from AppManager.DB_config import DatabaseManager
from AppManager.utils import save_model
import pickle as pkl


def test_DataBaseManagerFile():
    db_instance = DatabaseManager()
    
    conn = db_instance.connect_to_database()
    assert conn is not None, "Expected a valid connection object."
    assert isinstance(conn, sqlite3.Connection), "Expected an sqlite3.Connection instance"
    conn.close()
    
def test_utils_save_model():
    test_strin='test string'
    file_name = 'test'
    
    obj=save_model(object=test_strin, model_name=file_name)
    assert obj is None, 'Expacted a None value but got something else.'
    
    with open('Models/test.pkl', 'rb') as file:
        file_content = file.read()  # Read the file content as bytes
        result = pkl.loads(file_content)
        
    assert result == test_strin, 'does not match the saved model'    