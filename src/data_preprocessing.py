# Import necessary libraries
import pandas as pd
import os

# Define paths to the datasets (adjust according to your file structure)
creditcard_path = "C:/Users/user/Desktop/10 Academy- Machine-Learning/10 Academy W8 & 9/Data/creditcard.csv"
fraud_data_path = "C:/Users/user/Desktop/10 Academy- Machine-Learning/10 Academy W8 & 9/Data/Fraud_Data.csv"
ip_address_path = "C:/Users/user/Desktop/10 Academy- Machine-Learning/10 Academy W8 & 9/Data/IpAddress_to_Country.csv"

def load_data(file_path):
    """
    Loads a dataset from the specified file path.

    Args:
        file_path (str): Path to the dataset file.

    Returns:
        pd.DataFrame: Loaded dataset as a Pandas DataFrame.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return None
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {file_path}")
        return df
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

# Load datasets
creditcard_df = load_data(creditcard_path)
fraud_data_df = load_data(fraud_data_path)
ip_address_df = load_data(ip_address_path)

# Ensure datasets are loaded before proceeding
if creditcard_df is None or fraud_data_df is None or ip_address_df is None:
    print("Error: One or more datasets failed to load. Check file paths and formats.")
    exit()

# Display first few rows to understand data structure
print("\nCredit Card Data Sample:")
print(creditcard_df.head(), "\n")

print("Fraud Data Sample:")
print(fraud_data_df.head(), "\n")

print("IP Address Data Sample:")
print(ip_address_df.head(), "\n")

# Task 1: Handle Missing Values in Credit Card Data
def clean_creditcard_data(df):
    """
    Cleans the credit card dataset by handling missing values.

    Args:
        df (pd.DataFrame): Credit card dataset.

    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    print("Missing Values in Credit Card Data:")
    print(df.isnull().sum())

    # Drop rows with missing values
    df_cleaned = df.dropna()
    print("Credit card data cleaned. Rows with missing values dropped.\n")
    return df_cleaned

creditcard_df = clean_creditcard_data(creditcard_df)

# Task 2: Merge Fraud Data with IP Address Data
def merge_fraud_ip_data(fraud_df, ip_df):
    """
    Merges fraud transaction data with IP address data.

    Args:
        fraud_df (pd.DataFrame): Fraud transaction dataset.
        ip_df (pd.DataFrame): IP address dataset.

    Returns:
        pd.DataFrame: Merged dataset.
    """
    merged_df = pd.merge(fraud_df, ip_df, left_on="Ip", right_on="lower_bound_ip_address", how="left")
    print("Merged Fraud and IP Address Data Sample:")
    print(merged_df.head(), "\n")
    return merged_df

merged_fraud_df = merge_fraud_ip_data(fraud_data_df, ip_address_df)

# Task 3: Data Transformation
def transform_fraud_data(df):
    """
    Transforms fraud transaction data by ensuring numeric values in the 'Amount' column.

    Args:
        df (pd.DataFrame): Fraud transaction dataset.

    Returns:
        pd.DataFrame: Transformed dataset.
    """
    # Convert 'Amount' column to numeric, forcing invalid values to NaN
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

    # Remove rows where 'Amount' is missing
    df_cleaned = df.dropna(subset=['Amount'])
    
    print("Fraud Data Transformation Complete: Non-numeric values in 'Amount' handled.\n")
    return df_cleaned

fraud_data_df = transform_fraud_data(fraud_data_df)

# Define paths for processed data
processed_creditcard_data_path = "C:/Users/user/Desktop/10 Academy- Machine-Learning/10 Academy W8 & 9/data/processed_creditcard_data.csv"
processed_fraud_data_path = "C:/Users/user/Desktop/10 Academy- Machine-Learning/10 Academy W8 & 9/data/processed_fraud_data.csv"

def save_data(df, file_path):
    """
    Saves a DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): DataFrame to be saved.
        file_path (str): Destination file path.

    Returns:
        None
    """
    try:
        df.to_csv(file_path, index=False)
        print(f"Processed data saved at {file_path}")
    except Exception as e:
        print(f"Error saving file {file_path}: {e}")

# Save cleaned datasets
save_data(creditcard_df, processed_creditcard_data_path)
save_data(fraud_data_df, processed_fraud_data_path)

print("\nData preprocessing completed successfully!")
