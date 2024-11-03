import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Step 1: Visualize the Original Data (Feature Correlation)
# Create a DataFrame for visualization
feature_names = iris.feature_names
df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

# Display the correlation matrix
plt.figure(figsize=(8, 6))
correlation_matrix = df.corr()
plt.title('Feature Correlation Matrix')
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(feature_names)), feature_names, rotation=45)
plt.yticks(range(len(feature_names)), feature_names)
plt.show()

# Step 2: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Build and evaluate the model before feature selection
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy_before = accuracy_score(y_test, y_pred)
print(f'Accuracy before RFE: {accuracy_before:.4f}')

# Step 4: Apply RFE to select the top 2 features
rfe = RFE(estimator=model, n_features_to_select=2)
rfe.fit(X_train, y_train)

# Step 5: Transform the data to select the important features
X_train_rfe = rfe.transform(X_train)
X_test_rfe = rfe.transform(X_test)

# Step 6: Build and evaluate the model after feature selection
model.fit(X_train_rfe, y_train)
y_pred_rfe = model.predict(X_test_rfe)
accuracy_after = accuracy_score(y_test, y_pred_rfe)
print(f'Accuracy after RFE: {accuracy_after:.4f}')

# Step 7: Print the selected features
selected_features = np.array(feature_names)[rfe.support_]
print(f'Selected features: {selected_features}')
