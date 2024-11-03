import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_california_housing as load
from sklearn.model_selection import train_test_split as tts, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.feature_selection import RFE

data = load()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

print("Missing values in each feature:")
print(X.isnull().sum())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LinearRegression()
rfe = RFE(estimator=model, n_features_to_select=5)
rfe.fit(X_scaled, y)

selected_features = X.columns[rfe.support_]
print(f"Selected features: {selected_features.tolist()}")

X_train, X_test, y_train, y_test = tts(X_scaled, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Step 6: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse:.2f}')
print(f'R^2 Score: {r2:.2f}')

cross_val_scores = cross_val_score(model, X_scaled, y, cv=5, scoring='r2')
print(f'Cross-validated R^2 scores: {cross_val_scores}')
print(f'Mean Cross-validated R^2 score: {cross_val_scores.mean():.2f}')

# Step 7: Plot Actual Prices vs Predicted Prices
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, label='Predictions', color='blue', alpha=0.5)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual Prices vs Predicted Prices')

# Plot the diagonal line for reference
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', label='Perfect Prediction')

# Optional: Adding a line of best fit
sns.regplot(x=y_test, y=y_pred, scatter=False, color='orange', label='Best Fit Line')

plt.legend()
plt.show()

# Feature Importance Plot
importance = pd.DataFrame({'Feature': X.columns, 'Coefficient': model.coef_})
importance = importance.sort_values(by='Coefficient', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Coefficient', y='Feature', data=importance)
plt.title('Feature Importance in Multiple Linear Regression')
plt.show()
