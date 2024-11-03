# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline
# from sklearn.impute import SimpleImputer

# # Load data from CSV
# data = pd.read_csv('D:\\TMP\ADS CODES\\DS\\weather.csv')  # Change 'weather_data.csv' to your actual file path

# # Display the first few rows of the dataset
# print(data.head())

# # Define features and target
# X = data.drop('RainTomorrow', axis=1)  # Features (all columns except 'RainTomorrow')
# y = data['RainTomorrow']  # Target variable

# # Identify categorical and numerical columns
# categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
# numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

# # Check for missing values
# print(X.isnull().sum())

# # Create preprocessing pipelines
# numerical_transformer = Pipeline(steps=[
#     ('imputer', SimpleImputer(strategy='mean')),  # Fill missing numerical values with the mean
#     ('scaler', StandardScaler())  # Standardize numerical features
# ])

# categorical_transformer = Pipeline(steps=[
#     ('imputer', SimpleImputer(strategy='most_frequent')),  # Fill missing categorical values with the most frequent
#     ('onehot', OneHotEncoder(handle_unknown='ignore'))  # One-hot encode categorical features
# ])

# # Combine preprocessing steps using ColumnTransformer
# preprocessor = ColumnTransformer(
#     transformers=[
#         ('num', numerical_transformer, numerical_cols),
#         ('cat', categorical_transformer, categorical_cols)
#     ]
# )

# # Apply preprocessing
# X_processed = preprocessor.fit_transform(X)

# # Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)

# # Print the shapes of the resulting datasets
# print(f'Training data shape: {X_train.shape}, Test data shape: {X_test.shape}')



# Data Preprocessing

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('D:\\TMP\\ADS CODES\\DS\\weather.csv')
print(data)

# handling missing values
print(data.isnull().sum())
cleared_data = data.dropna()
print(cleared_data.isnull().sum())
data['WindGustSpeed'] = data['WindGustSpeed'].fillna(data['WindGustSpeed'].mean())

from sklearn.feature_selection import SelectKBest as skb, f_classif as fc

# x = encodeddata.drop('targetcolumn', axis=1)
# y = encodeddata['targetcolumn']
# selector = skb(k=5, score_func=fc)
# selector.fit(x, y)
# print(x.columns[selector.get_support()])