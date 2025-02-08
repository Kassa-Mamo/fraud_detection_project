import lime
from lime.lime_tabular import LimeTabularExplainer
import joblib
import pandas as pd

def explain_with_lime(model, X_train):
    """ Explain the model predictions using LIME """
    explainer = LimeTabularExplainer(X_train, training_labels=y_train, mode='classification')
    exp = explainer.explain_instance(X_train.iloc[0], model.predict_proba)
    exp.show_in_notebook()
    return exp
