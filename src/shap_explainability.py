 import shap
import joblib
import pandas as pd

def explain_with_shap(model, X_train):
    """ Explain the model predictions using SHAP """
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_train)
    shap.summary_plot(shap_values, X_train)
    return shap_values

