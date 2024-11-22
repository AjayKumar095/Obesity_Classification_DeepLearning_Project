# Add the root directory to the sys.path
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect
from AppManager.DB_config import DatabaseManager
from AppManager.logger import logging
from AppManager.utils import LoadModel
import pandas as pd 

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method != 'POST':
        return redirect('index')
    
    else :
        data = {
            'Gender': request.form.get('Gender'),
             'Age':request.form.get('Age'),
             'Height':request.form.get('Height'),
             'Weight':request.form.get('Weight'),
            'family_history_with_overweight':request.form.get('family_history_with_overweight'),  
             'FAVC':request.form.get('FAVC'),
              'FCVC':request.form.get('FCVC'), 
             'NCP':request.form.get('NCP'),
              'CAEC':request.form.get('CAEC'),
              'SMOKE':request.form.get('SMOKE'),
              'CH2O':request.form.get('CH2O'),
              'SCC':request.form.get('SCC'),
              'FAF':request.form.get('FAF'),
              'TUE':request.form.get('TUE'),
              'CALC':request.form.get('CALC'),
             'MTRANS':request.form.get('MTRANS'),
        }
        logging.info(data)
        df= pd.DataFrame(data=data)
        model=LoadModel()
        
        preprocessor=model.load_preprocessor()
        process_data = preprocessor.transform(df)
        logging.info(f'processed data{process_data}')
        #ANN_model = model.load_model()
        
        #predicted_value_list=ANN_model.predict(process_data)
        return redirect('index')

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0")