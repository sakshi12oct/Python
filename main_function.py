""" if __name__ == '__main__':: This is a standard Python idiom. 
The code inside this block will only run if the script is executed directly (not when it's imported as a module in another script)
"""

def add(**a):
    for key, value in a.items():
        print(f"{key}: {value}")

if __name__ == '__main__':
    add(a=20, b=30, c=60, d=90, e=60, f=70, g=50, h=60, i=45)

 
""" to calculate the sum of the values associated with the keyword arguments. Here's the updated code: """

def add(**a):
    total = 0
    for key, value in a.items():
        total += value
    return total

if __name__ == '__main__':
    result = add(a=20, b=30, c=60, d=90, e=60, f=70, g=50, h=60, i=45)
    print("Sum of values:", result)
