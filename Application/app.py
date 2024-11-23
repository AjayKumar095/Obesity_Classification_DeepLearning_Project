# Add the root directory to the sys.path
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect
from AppManager.DB_config import DatabaseManager
from AppManager.logger import logging
from AppManager.utils import LoadModel
import pandas as pd 
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    try:
        logging.info('rendering index page')
        return render_template('index.html')
    except Exception as e:
        logging.info(f'Haing some error while rendering index page. Error:- {e}')
        return """<h1 style="color:red"><center>404 Page Not Found !!!</center></h1>"""


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method != 'POST':
        logging.info('Form methos does not match to post.')
        return render_template('index.html')
    
    else :
        logging.info('Collecting data from frontend.')
        data = {
            'Gender': request.form.get('Gender'),
             'Age': float(request.form.get('Age')),
             'Height': float(request.form.get('Height')),
             'Weight': float(request.form.get('Weight')),
            'family_history_with_overweight':request.form.get('family_history_with_overweight'),  
             'FAVC':request.form.get('FAVC'),
              'FCVC':float(request.form.get('FCVC')), 
             'NCP':float(request.form.get('NCP')),
              'CAEC':request.form.get('CAEC'),
              'SMOKE':request.form.get('SMOKE'),
              'CH2O':float(request.form.get('CH2O')),
              'SCC':request.form.get('SCC'),
              'FAF':float(request.form.get('FAF')),
              'TUE':float(request.form.get('TUE')),
              'CALC':request.form.get('CALC'),
             'MTRANS':request.form.get('MTRANS'),
        }
        logging.info("Collected data",data)
        df= pd.DataFrame(data=data, index=[0])
        model=LoadModel()
        
        logging.info('Preprocessing the collecting data.')
        preprocessor=model.load_preprocessor()
        process_data = preprocessor.transform(df)
        logging.info(f'processed data{process_data}')
        
        logging.info('Loading the ANN model.')
        ANN_model = model.load_model()
        logging.info('Predicting obesity level on collectd data.')
        predicted_value_list=ANN_model.predict(process_data)
        logging.info(f'predicted value {predicted_value_list}')
        
        
        target_category_rank = {
                'Normal Weight': 0,
                'Insufficient Weight': 1,
                'Overweight Level I': 2,
                'Overweight Level II': 3,
                'Obesity Type I': 4,
                'Obesity Type II': 5,
                'Obesity Type III': 6
            }
        # Step 2: Reverse the dictionary
        rank_to_category = {v: k for k, v in target_category_rank.items()}
        # Step 4: Get the index of the maximum probability
        predicted_rank = np.argmax(predicted_value_list[0])

       # Step 5: Map the index to the class label
        predicted_category = rank_to_category[predicted_rank]
        
        obesity_percentage=(predicted_rank+1/8)*100
        logging.info(f'predicted category {predicted_category}, {predicted_rank}')
        
        return render_template('index.html', level=obesity_percentage, obesity_class=predicted_category)

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0")