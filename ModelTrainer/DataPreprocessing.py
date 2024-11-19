# Add the root directory to the sys.path
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


## Main code start from here..

from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from AppManager.logger import logging
from AppManager.DB_config import DatabaseManager
from AppManager.utils import save_model
import pandas as pd

class preprocessing:
    
    def __init__(self):
        pass
    
    def preprocess(self):
        logging.info('Data prerocessing start.')
        
        try:
            logging.info('connecting to database.')
            db_instance=DatabaseManager()
            conn = db_instance.connect_to_database()
            logging.info(f'Connected to database, {conn}')
            
            query="SELECT * FROM HealthData"
            df = pd.read_sql_query(query, conn)
            logging.info(f'{df.head(1).to_string()}')
            
            input_df = df.iloc[:,:-1]
            ## Defining the numerical, ordinal and nominal features.
            logging.info(' Defining the numerical, ordinal and nominal features.')
            num_cols = [col for col in input_df.columns if input_df[col].dtype != 'object']

            nominal_cols = ['Gender', 'family_history_with_overweight', 'FAVC', 'SMOKE', 'SCC', 'MTRANS']

            ordinal_cols = [ 'CALC', 'CAEC']
            
            logging.info(f'{num_cols.len()}, {nominal_cols.len()}, {ordinal_cols.len()}')
            ## Building pipeline for data transformation
            logging.info(' Building pipeline for data transformation.')
            # For numerical features: impute with median and scale the data
            numerical_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])

            # For nominal features: impute with most frequent and encoded respectively 
            nominal_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('OneHotEncoder', OneHotEncoder(handle_unknown='ignore'))
            ])

            # For nordinal features: impute with most frequent and encoded respectively 
            ordinal_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('OrdinalEncoder', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1))
            ])


            # ColumnTransformer to apply different transformations to different columns
            logging.info('ColumnTransformer to apply different transformations to different columns.')
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', numerical_transformer, num_cols),
                    ('nom', nominal_transformer, nominal_cols),
                    ('ord', ordinal_transformer, ordinal_cols),
                ]
            )

            target_category_rank = {
                'Normal_Weight': 1,
                'Insufficient_Weight': 2,
                'Overweight_Level_I': 3,
                'Overweight_Level_II': 4,
                'Obesity_Type_I': 5,
                'Obesity_Type_II': 6,
                'Obesity_Type_III': 7
            }
            
            # Fit the preprocessor on the training data
            # Fit and transform the features
            df_transformer = preprocessor.fit_transform(input_df)
            save_model(object=preprocessor, model_name='preprocessor.pkl')
            
            # replace the targent feature into numerical.
            target = df['NObeyesdad'].replace(target_category_rank)
          
            
            # Extract feature names from the transformers
            # For numerical features, the feature names remain the same
            num_feature_names = num_cols

            # For nominal features, extract feature names from OneHotEncoder
            nominal_feature_names = preprocessor.transformers_[1][1].named_steps['OneHotEncoder'].get_feature_names_out(nominal_cols)

            # For ordinal features, the feature names remain the same
            ordinal_feature_names = ordinal_cols

            # Combine all feature names
            inputs_feature_names = num_feature_names + nominal_feature_names.tolist() + ordinal_feature_names

            
            Input_df = pd.DataFrame(df_transformer, columns=inputs_feature_names)
            logging.info(Input_df.head(1).to_string)
            return (Input_df, target)
            
        except Exception as e:
            logging.info(f'An error occure while data processing. Error: - {e}')
            return


test = preprocessing()

test.preprocess()