# Assignment Statements: These are used to assign values to variables. For example:

x = 5
name = "John"


# Expression Statements: These involve expressions, which can include arithmetic operations, function calls, etc. For example:

result = x + 10
print("Hello, World!")


# Conditional Statements (if, elif, else): These are used for decision-making based on conditions. For example:

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")


# Looping Statements (for, while): These allow you to repeat a block of code multiple times. For example:

for i in range(5):
    print(i)

while x > 0:
    print(x)
    x -= 1


# Function Definition Statements: These define reusable functions. For example:

def greet(name):
    print("Hello, " + name + "!")


# Import Statement to Access Libraries and Functions:

# Importing the 'math' library/module
import math

# Using a function from the 'math' module

square_root = math.sqrt(16)
print("Square root of 16:", square_root)


# Importing only the 'sqrt' function from the 'math' module

from math import sqrt

# Using the 'sqrt' function directly without 'math' prefix

square_root = sqrt(25)
print("Square root of 25:", square_root)
