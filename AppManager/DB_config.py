## This file contain methods to config the data base and its query's.
## main code start here..

import os
import sqlite3
import pandas as pd 

class DatabaseManager():
    __database_path = os.path.join('DataBase', 'TrainingData.db')
    
    def __init__(self):
        pass
    
    @classmethod
    def connect_to_database(self):
        
        """_summary_   : This method is use to make connection with the database and
            return the connection object to the caller of this method,
        """
        try:
           conn = sqlite3.connect(database=self.__database_path, timeout=10) 
           return conn
        
        except ValueError as e:
            ## add logg here
         
            return None
        
         