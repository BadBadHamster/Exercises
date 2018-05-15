# Exercise 10 - Arithmetic

# Read input from user
a = int(input("Please enter a \n"))
b = int(input("Please enter b \n"))

import math

# Print the results of calculations
print()
print("Sum of a+b =", a + b)
print("Difference of b-a =", b - a)
print("Product of a*b =", a * b)
print("Quotient of a/b =", a / b)
print("Reminder of a/b =", a % b)  # reminder is represented by %
print("Logarythm Log10 from a =", math.log10(a))  # before using math fucntion they should be imported - line 7
print("a to the power of b equals", math.pow(a, b))
