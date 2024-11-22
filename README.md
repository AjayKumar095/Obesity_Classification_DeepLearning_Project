Obesity Classification Using ANN - Project README

This project implements an Artificial Neural Network (ANN) model to classify obesity levels based on user inputs. The model is trained on obesity classification data and predicts the obesity level, providing valuable insights for users. The project is built with Flask for web deployment, and it also includes various utilities, data preprocessing, and model training pipelines.

---

Table of Contents:
1. Project Structure
2. Technologies & Requirements
3. Installation & Setup
4. Usage
5. Links & Resources

---

Project Structure:

Here’s the folder structure of the project:

Obesity-Classification/
│
├── Application/                  # Flask web application
│   ├── app.py                     # Main Flask app
│   ├── Modules/                   # Custom modules used in the app
│   ├── static/                    # Static files (CSS, JS, images)
│   └── Templates/                 # HTML templates
│
├── AppManager/                  # Utility functions for the app
│   ├── utils.py                  # Utility functions
│   ├── DB_config.py              # Database configuration
│   └── logger.py                 # Logging configuration
│
├── ModelTrainer/                # Model training pipeline
│   ├── DatapreProcessing.py      # Data preprocessing script
│   └── Trainer.py                # Model training script
│
├── Models/                       # Stored model files
│   └── ann_model.keras 
|   |__ preprocessor.pkl          # Trained model pickle file
│
├── Research/                                 # Jupyter notebooks for research & data analysis
│   └── HyperPerimeterTuning.ipynb            # Data analysis notebook
│
└── Database/                      # SQLite database files
    ├── DB_query.sql               # Database file
    └── TrainingData.db            # SQL schema file

---

Technologies & Requirements:

This project uses several popular libraries and tools for data processing, model training, and deployment. Below are the dependencies for this project:

Core Requirements:
- Flask: A micro web framework used to serve the web application.
- Flask-Cors: Handles Cross-Origin Resource Sharing (CORS) for Flask, allowing requests from different origins.
- TensorFlow: A deep learning framework used to build and train the ANN model.
- Keras: A high-level API used for building and training neural networks, integrated with TensorFlow.
- Keras-Tuner: Used for hyperparameter tuning during the model training process.
- Pandas: A data manipulation library to handle data preprocessing.
- Matplotlib: A plotting library used for data visualization and plotting graphs.
- Seaborn: A statistical data visualization library built on top of Matplotlib.
- Transformers: A library for natural language processing, if needed for feature extraction or additional model components.
- Docker: Containerization tool used to deploy the app in a consistent environment.
- scikit-learn: A machine learning library for data processing, model evaluation, and metrics.
- Gunicorn: A WSGI HTTP server to run the Flask application in production.
- Flask-WTF: Provides integration with WTForms for handling web forms securely.
- Werkzeug: A comprehensive WSGI web server library that Flask relies on for handling HTTP requests.

Installation of Dependencies:
You can install the required dependencies by running the following command:

pip install -r requirements.txt

The `requirements.txt` file includes all of the dependencies mentioned above.

---

Installation & Setup:

To get this project up and running on your local machine:

1. Clone the repository:
    git clone https://github.com/yourusername/obesity-classification.git
    cd obesity-classification

2. Create a virtual environment (optional but recommended):
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate

3. Install dependencies:
    pip install -r requirements.txt

4. Run the Flask app:
    python Application/app.py

    The app will be accessible at http://127.0.0.1:5000/.

---

Usage:

1. Input Data: 
   Navigate to the web interface and fill out the form with the required user data. This will include various health metrics such as weight, height, age, etc.
   
2. Model Prediction:
   Once the form is submitted, the ANN model processes the input and predicts the user's obesity level.

3. Results: 
   The app will display the predicted obesity level and provide additional insights based on the classification.

---

Links & Resources:

- Docker Image: [Docker Image Repository](https://hub.docker.com/repository/docker/yourusername/obesity-classification)
- LinkedIn: [My LinkedIn Profile](https://www.linkedin.com/in/ajay-kumar-4b1b7329a/)

---

Images:

Here are some screenshots from the project:

![Obesity Prediction Form](Application\static\Assets\projectimage1.png)
*Obesity prediction form where users enter their data.*

![Obesity Prediction Result](Application\static\Assets\projectimage2.png)
*Result page showing the predicted obesity level.*

---

Conclusion:

This project demonstrates how an ANN model can be used to classify obesity levels based on user input. The Flask web application provides a simple interface for users to interact with the model and receive predictions. The code is well-structured with different folders dedicated to specific functionalities, making it easy to maintain and extend.

Feel free to contribute or reach out with any questions!
