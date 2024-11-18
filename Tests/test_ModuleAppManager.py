# Add the root directory to the sys.path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

## PyTest
import pytest 
import sqlite3
from AppManager.DB_config import DatabaseManager


def test_DataBaseManagerFile():
    db_instance = DatabaseManager()
    
    conn = db_instance.connect_to_database()
    assert conn is not None, "Expected a valid connection object."
    assert isinstance(conn, sqlite3.Connection), "Expected an sqlite3.Connection instance"
    conn.close()
    
