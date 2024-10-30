# Nairobi Office Price Prediction

This project uses simple linear regression to predict office prices based on office size. It implements gradient descent to find the optimal line of best fit and uses Mean Squared Error (MSE) as a performance metric. The model is trained on the Nairobi Office Price Ex dataset.

## Problem Definition

The objective is to:
1. Implement a function to compute Mean Squared Error (MSE) as a performance measure.
2. Implement a Gradient Descent algorithm to learn the best-fit line by updating the weights (slope and intercept).
3. Train the model with 10 epochs and display the MSE after each epoch.
4. Plot the line of best fit.
5. Predict the price of a 100 sq. ft. office using the trained model.

## Project Structure

- `data.csv`: The dataset file containing `SIZE` (office size in square feet) and `PRICE` (office price) columns.
- `main.py`: The main code file containing functions and training logic.

## Code Overview

1. **mean_squared_error**: Calculates the Mean Squared Error between actual and predicted values.
2. **gradient_descent**: Implements the gradient descent algorithm to update the slope (m) and intercept (c) of the line.
3. **Training Loop**: Iterates through 10 epochs, updating `m` and `c` using gradient descent and printing the MSE after each epoch.
4. **Plotting**: After training, the data points and the line of best fit are plotted using Matplotlib.
5. **Prediction**: Uses the final model to predict the price of an office of size 100 sq. ft.

## Requirements

To run this project, you need:
- Python 3
- NumPy
- Pandas
- Matplotlib

You can install these dependencies using:
```bash
pip install numpy pandas matplotlib
```

## Instructions

1. **Load Dataset**: Ensure `data.csv` is in the same directory as `main.py`.
2. **Run the Code**: Execute `main.py` to train the model, view the MSE at each epoch, and display the plot.
   ```bash
   python main.py
   ```
3. **Output**: 
   - The code will print the MSE after each epoch.
   - A graph showing the line of best fit alongside the data points will be displayed.
   - The predicted price for a 100 sq. ft. office will be printed at the end.

## Sample Output

```plaintext
Epoch 1: MSE = 212.4863671319134
...
Epoch 10: MSE = 75.0066929066985
The predicted price for a 100 sq. ft. office is: 135.60926686884739
```

## Results

After 10 epochs, the model approximates a line of best fit. The prediction for the price of a 100 sq. ft. office is output based on the trained model.

