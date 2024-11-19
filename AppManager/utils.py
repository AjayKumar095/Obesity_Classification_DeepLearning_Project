### In this file we add some helper functions or methods.
from pyexpat import model
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pickle as pkl
from AppManager.logger import logging
import keras
import sqlite3
import numpy as np
import pandas as pd 
## Method to save the model.
def save_model(object, model_name:str):
    
    try:
        logging.info('Checking for model file path.')
        model_file_path='Models'
        logging.info(f'{model_file_path}, outside if block.')
        
        if not model_file_path:
            logging.info('Creating model file path if not exist.')
            os.makedirs(model_file_path)
            logging.info(f'{model_file_path}, inside if block')
            
        if not object or not model_name:
            logging.info('Either object or model name is none type or empty.')
            return 
        
        else:
            logging.info('Creating the model file.')
            file_path = os.path.join(model_file_path, model_name)
            logging.info(file_path)
            with open(file_path, 'wb') as file:
                pkl.dump(obj=object, file=file)
                logging.info('Model saved.')
            
    except Exception as e:
        logging.info(f'Error occure while saving the model. {e}.')
        


## Load model

class LoadModel():
    
    def __init__(self):
         pass 
     
    def load_preprocessor(self):
        
        # Models\preprocessor.pkl
        
        file_path= os.path.join('Models', 'preprocessor.pkl')
        
        with open(file=file_path, mode='rb') as file:
            preprocessor = pkl.load(file)
            
        return preprocessor
    
    def load_model(self):
        
        # Models\ann_model.keras
        file_path= os.path.join('Models', 'ann_model.keras')
        
        model = keras.models.load_model(filepath=file_path)
        
        return model
    

conn = sqlite3.connect('DataBase/TrainingData.db')


df = pd.read_sql_query("SELECT * FROM HealthData LIMIT 1;", conn)

input_data = df.iloc[:,:-1]

input_data = np.array(input_data)

models= LoadModel()

process = models.load_preprocessor()

processed_data = process.transform(input_data)
print(processed_data)