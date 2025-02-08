# Fraud Detection Project

## 1️⃣ Overview
This project aims to improve fraud detection in e-commerce and banking transactions using machine learning techniques. It includes **data preprocessing, exploratory data analysis (EDA), model training, evaluation, and explainability.**

---

## 2️⃣ Code Execution Flow (How to Run)
### **Step 1: Data Preprocessing & Cleaning**
- **Run:** `notebooks/data_analysis_and_preprocessing.ipynb`
- **Purpose:** Cleans and prepares raw fraud data.
- **Input:** Raw dataset stored in the `data/` folder.
- **Output:** Processed data saved in `data/processed/processed_fraud_data.csv`.

### **Step 2: Model Training**
- **Run:** `src/model_building.py`
- **Purpose:** Trains a fraud detection model using machine learning.
- **Input:** `data/processed/processed_fraud_data.csv`
- **Output:** Saved model in `models/fraud_model.pkl`.

### **Step 3: Model Deployment (API)**
- **Run:** `src/flask_api.py`
- **Purpose:** Serves the trained model as an API.
- **Start API:**  
  ```sh
  python src/flask_api.py
