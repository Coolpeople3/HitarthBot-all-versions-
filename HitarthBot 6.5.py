# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import numpy as np

# Generate sample data (you can replace this with your own dataset)
X, y = make_regression(n_samples=100, n_features=1, noise=10)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a linear regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Test the model on the test data
predictions = model.predict(X_test)

# Output the results
print("Predicted values:", predictions)
print("Actual values:", y_test)
