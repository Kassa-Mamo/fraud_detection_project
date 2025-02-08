 from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

def build_model(X_train, y_train):
    """ Build and train a Random Forest model """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """ Evaluate the model performance """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return accuracy, cm

def save_model(model, filename):
    """ Save the trained model to disk """
    joblib.dump(model, filename)

def load_model(filename):
    """ Load the model from disk """
    model = joblib.load(filename)
    return model

