 
## Project Overview

The Fraud Detection Project leverages machine learning to detect fraudulent transactions in a financial dataset. The project follows a comprehensive process that includes data preprocessing, feature engineering, model building, training, and model explainability through SHAP and LIME.

## Steps

### 1. **Data Analysis and Preprocessing** (`notebooks/data_analysis_and_preprocessing.ipynb`)

This notebook focuses on:
- **Exploratory Data Analysis (EDA)**: It involves understanding the data, its distribution, and any missing values or anomalies.
- **Data Cleaning**: Handle missing values, duplicates, and perform necessary transformations.
- **Feature Engineering**: Create additional features like "Amount_Range" to enhance the model's predictive capabilities.

### 2. **Model Building and Training** (`notebooks/model_building_and_training.ipynb`)

This notebook covers:
- Splitting the dataset into training and testing sets.
- Training a **Random Forest Classifier** to predict fraudulent transactions.
- Evaluating the model performance using metrics like precision, recall, and confusion matrix.
- Saving the trained model to a `.pkl` file for later use.

### 3. **Model Explainability** (`notebooks/model_explainability.ipynb`)

This notebook explains the model's predictions using:
- **SHAP (SHapley Additive exPlanations)**: Visualizes feature importance and interprets the model’s decisions.
- **LIME (Local Interpretable Model-agnostic Explanations)**: Provides local interpretability for individual predictions.

### 4. **API Development** (`src/flask_api.py`)

A Flask API is built to:
- Serve the trained machine learning model.
- Accept incoming requests for fraud prediction.
- Log requests in `api_requests.log` for monitoring and debugging.

### 5. **Model Serving and Dashboard** (`src/serve_model.py`, `src/dashboard.py`)

- **Model Serving**: Exposes the model through the Flask API for real-time predictions.
- **Dashboard**: A dashboard for monitoring model performance, logs, and visualizations.

### 6. **Testing** (`tests/`)

The project includes unit tests to ensure that:
- The API is working correctly.
- The machine learning model performs as expected.
- Data preprocessing and feature engineering steps are functioning properly.

## Requirements

Install all the required dependencies using:


