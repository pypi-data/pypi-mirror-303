# Linear Regression Package

`linear_regression` is a Python library for implementing simple linear regression.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `linear_regression`.

```bash
pip install linear_regression

## Usage

```python
from linear_regression import SimpleLinearRegression

# Create a SimpleLinearRegression object
model = SimpleLinearRegression()

# Prepare your data
X = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Fit the model
model.fit(X, y)

# Make predictions
predictions = model.predict([6, 7, 8])
print(predictions)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

