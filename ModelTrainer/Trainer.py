# Add the root directory to the sys.path
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


## Main code start here..

from AppManager.DB_config import DatabaseManager
from AppManager.logger import logging
from AppManager.utils import save_model
from ModelTrainer.DataPreprocessing import preprocessing
from sklearn.model_selection import train_test_split
from keras.src.callbacks import EarlyStopping
from keras.src.regularizers import L2
from keras.src.layers import Dense, Dropout
from keras.src.utils import to_categorical
from keras.src.optimizers import Adam
from keras.src.models import Sequential

class ModelTraining():
    
    def __init__(self):
        pass


    def train_model(self):
        
        try:
            
            preprocess = preprocessing()
            
            X, y = preprocess.preprocess()
            
            x_train,  x_test, y_train , y_test =train_test_split(X, y, test_size=0.2, random_state=42)
            y_train_hp_cat = to_categorical(y_train)
            y_test_hp_cat = to_categorical(y_test)
            

            ## Building the ANN model again with L2 regularizers to reduce the Overfitting.

            model=Sequential()

            ## Input layer
            model.add(Dense(32, activation='relu', input_shape=(x_train.shape[1],), kernel_regularizer=L2(0.001) ))

            ## hidden and dropout layer 1
            model.add(Dense(224, activation='relu', kernel_regularizer=L2(0.001)))
            model.add(Dropout(0.2))

            ## hidden and dropout layer 2
            model.add(Dense(32, activation='relu', kernel_regularizer=L2(0.001)))
            model.add(Dropout(0.4))

            ## hidden and dropout layer 3
            model.add(Dense(48, activation='relu', kernel_regularizer=L2(0.001)))
            model.add(Dropout(0.4))

            ## Output Layer.
            model.add(Dense(8, activation='softmax'))



            # Compile the Model
            model.compile(optimizer=Adam(learning_rate=0.01), loss='categorical_crossentropy', metrics=['accuracy'])
            early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
            ## Train the model

            model.fit(x_train, y_train_hp_cat, epochs=500, batch_size=32, validation_split=0.2, callbacks=[early_stopping])
           
            # Define the path where you want to save the model
            desired_folder = 'Models'  # Specify your folder here
            os.makedirs(desired_folder, exist_ok=True)  # Create the folder if it doesn't exist

            # Define the model file path
            model_file_path = os.path.join(desired_folder, 'ann_model.keras')
            
            # Save the model in .h5 format 
            logging.info('Save the model in .h5 format t')
            model.save(model_file_path)
            
            logging.info(f'Model file path = {model_file_path}')
            
            test_loss, test_accuracy = model.evaluate(x_test, y_test_hp_cat)
            
            logging.info(f'Test loss: {test_loss}, test accuracy = {test_accuracy}')
            print(f'Test Loss: {test_loss}')
            print(f'Test Accuracy: {test_accuracy}')
            
            return 'training done'
        
        except Exception as e:
            logging.debug(f'An error occur while model training. Error: - {e}')
            return


test_train = ModelTraining()

print(test_train.train_model())