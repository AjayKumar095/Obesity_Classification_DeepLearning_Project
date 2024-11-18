### In this file we add some helper functions or methods.
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pickle as pkl
from AppManager.logger import logging
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
            file_path = os.path.join(model_file_path, f"{model_name}.pkl")
            logging.info(file_path)
            with open(file_path, 'wb') as file:
                pkl.dump(obj=object, file=file)
                logging.info('Model saved.')
            
    except Exception as e:
        logging.info(f'Error occure while saving the model. {e}.')
        
    