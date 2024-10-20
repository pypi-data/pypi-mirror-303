# Linear Regression

This repository contains a simple implementation of a Linear Regression model using Python and NumPy.

## Overview

The `LinearRegression` class implements a basic linear regression model with gradient descent optimization. The model can be trained on a dataset and used to make predictions.

## Installation

To use this code, you need to have Python and NumPy installed. You can install NumPy using pip:

```sh
pip install numpy
pip install linear_reg_youcef
```

## Usage

### Importing the Module

First, import the necessary module:

```python
import numpy as np
from linear_reg_youcef import LinearRegression
```

### Creating the Model

Create an instance of the `LinearRegression` class by passing the input data (`x`) and the target labels (`y`):

```python
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
model = LinearRegression(x, y)
```

### Training the Model

Train the model using the `fit` method. You need to specify the number of epochs and the learning rate:

```python
epochs = 1000
learning_rate = 0.01
model.fit(epochs, learning_rate)
```

### Making Predictions

Use the `predict` method to make predictions on new data:

```python
new_data = np.array([6, 7, 8])
predictions = model.predict(new_data)
print(predictions)
```

## Code Explanation

### LinearRegression Class

- `__init__(self, x, y)`: Initializes the model with input data `x` and target labels `y`. It also initializes the parameters `m` (slope) and `b` (intercept) to 0, and calculates the number of data points `n`.

- `fit(self, epochs, lr)`: Trains the model using gradient descent. It updates the parameters `m` and `b` over a specified number of epochs with a given learning rate `lr`.

- `predict(self, inp)`: Makes predictions on new input data `inp` using the trained model parameters.

## License
[MIT](https://choosealicense.com/licenses/mit/)