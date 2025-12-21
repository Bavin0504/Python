import math 

def calculations(num):
    square_root = math.sqrt(num)
    logarithm = math.log(num)
    sine = math.sin(num)
    return square_root, logarithm, sine

num = int(input("Enter a number: "))
square_root, logarithm, sine = calculations(num)
print(f"Square Root: {square_root}")
print(f"Logarithm: {logarithm}")
print(f"Sine: {sine}")