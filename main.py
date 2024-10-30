import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('data.csv')

# Extract 'SIZE' and 'PRICE' columns
x = data['SIZE'].values
y = data['PRICE'].values

# Function to compute Mean Squared Error
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Gradient Descent function to update slope (m) and intercept (c)
def gradient_descent(x, y, m, c, learning_rate):
    N = len(y)
    y_pred = m * x + c  # Predicted values
    # Calculate gradients
    dm = (-2/N) * np.sum(x * (y - y_pred))
    dc = (-2/N) * np.sum(y - y_pred)
    # Update m and c
    m -= learning_rate * dm
    c -= learning_rate * dc
    return m, c

# Initialize parameters
m = np.random.rand()  # Random slope
c = np.random.rand()  # Random intercept
learning_rate = 0.0001  # Adjusted learning rate
epochs = 10

# Training loop
for epoch in range(epochs):
    m, c = gradient_descent(x, y, m, c, learning_rate)
    y_pred = m * x + c  # Predicted values with updated parameters
    error = mean_squared_error(y, y_pred)  # Calculate MSE
    print(f"Epoch {epoch+1}: MSE = {error}")

# Plot the data points and the line of best fit
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, y_pred, color='red', label='Line of Best Fit')
plt.xlabel('Office Size (sq. ft.)')
plt.ylabel('Office Price')
plt.legend()
plt.show()

# Predict the price for a 100 sq. ft. office
size = 100
predicted_price = m * size + c
print(f"The predicted price for a 100 sq. ft. office is: {predicted_price}")
