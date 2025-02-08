# Import necessary libraries
import pandas as pd

# Paths to the datasets (adjusted according to your file structure)
creditcard_path = "C:/Users/user/Desktop/10 Academy- Machine-Learning/10 Academy W8 & 9/Data/creditcard.csv"
fraud_data_path = "C:/Users/user/Desktop/10 Academy- Machine-Learning/10 Academy W8 & 9/Data/Fraud_Data.csv"
ip_address_path = "C:/Users/user/Desktop/10 Academy- Machine-Learning/10 Academy W8 & 9/Data/IpAddress_to_Country.csv"

# Load the datasets
creditcard_df = pd.read_csv(creditcard_path)
fraud_data_df = pd.read_csv(fraud_data_path)
ip_address_df = pd.read_csv(ip_address_path)

# Display first few rows of each dataframe to understand structure
print("Credit Card Data:")
print(creditcard_df.head(), "\n")

print("Fraud Data:")
print(fraud_data_df.head(), "\n")

print("IP Address Data:")
print(ip_address_df.head(), "\n")

# Task 1: Data Preprocessing for credit card data
# Check for missing values
print("Missing Values in Credit Card Data:")
print(creditcard_df.isnull().sum())

# Handle missing values (if any)
# For simplicity, let's drop rows with missing values (you can choose to fill them instead)
creditcard_df = creditcard_df.dropna()

# Task 2: Combine data (if necessary)
# For this task, we'll just show how to merge based on a common field, assuming 'Ip' is common
# Ensure the column name in fraud_data_df and ip_address_df matches for merging
merged_df = pd.merge(fraud_data_df, ip_address_df, left_on="Ip", right_on="lower_bound_ip_address", how="left")

# Check the resulting merged data
print("Merged Data (Fraud + IP Address Data):")
print(merged_df.head(), "\n")

# Task 3: Data Transformation
# If needed, let's convert the 'Amount' feature to numeric values (handle any non-numeric values)
fraud_data_df['Amount'] = pd.to_numeric(fraud_data_df['Amount'], errors='coerce')

# Handle any new missing values in 'Amount'
fraud_data_df = fraud_data_df.dropna(subset=['Amount'])

# Final output of processed data
processed_creditcard_data_path = "C:/Users/user/Desktop/10 Academy- Machine-Learning/10 Academy W8 & 9/data/processed_creditcard_data.csv"
processed_fraud_data_path = "C:/Users/user/Desktop/10 Academy- Machine-Learning/10 Academy W8 & 9/data/processed_fraud_data.csv"

# Save cleaned data
creditcard_df.to_csv(processed_creditcard_data_path, index=False)
fraud_data_df.to_csv(processed_fraud_data_path, index=False)

print(f"Processed data saved at {processed_creditcard_data_path} and {processed_fraud_data_path}")
