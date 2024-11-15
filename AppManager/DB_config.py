## This file contain methods to config the data base and its query's.

## Sample method, not for any use.
def sample_connect(db_name:str):
    return f'Connected to {db_name}.'
    

import re
import sqlite3
import pandas as pd 

class DatabaseManager():
    
    def __init__():
        pass
        
    def connect_to_database(self, db_name:str):
        
        """_summary_   : This method is use to make connection with the database and
            return the connection object to the caller of this method,
            This function take one arrgunment as database file path as string.
        """
        try:
            
           conn = sqlite3.connect(database=db_name, timeout=10) 
           return conn   
        
        except ValueError as e:
            ## add logg here
            conn = None
            return conn