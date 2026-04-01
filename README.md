# Pima Indians Diabetes Prediction

This project is a machine learning-based web application that predicts whether a patient is likely to have diabetes using the Pima Indians Diabetes dataset.

## Overview

The objective of this project is to build a predictive model using patient health data and deploy it as a web application for real-time predictions.

## Project Structure
- templates # HTML templates for web interface
- main.py # Flask app for prediction UI
- train.py # Script to train the model
- test.py # Script to test the model
- train.csv # Dataset used for training
- model_file.pkl # Saved trained model
- model_file_pickle.pkl # Alternative saved model file


## What I Implemented

- Data preprocessing and cleaning  
- Feature selection from medical dataset  
- Model training using machine learning algorithms  
- Model evaluation using test data  
- Saving trained models using pickle (`.pkl`)  
- Built a Flask web app for user input and predictions  

## Model Details

- Classification problem (Diabetes vs Non-Diabetes)  
- Trained using patient health features  
- Model saved and loaded using pickle files  
- Used for real-time predictions in the web app  

## Tech Stack

- Python  
- Scikit-learn  
- Pandas, NumPy  
- Flask (for deployment)  
- HTML (templates)
