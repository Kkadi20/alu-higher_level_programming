#!/usr/bin/python3

# Import the specific functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Define the variables
a = 10
b = 5

# Use exactly 4 print functions to display the results
print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

# Ensure the code is not executed when imported
if __name__ == "__main__":
    pass
