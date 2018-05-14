# Exercise 7 - Sum of the first n Positive Integeres

# Compute the sum of the first n positive integers

# Read input from the user
n = int(input("enter a positive integer: \n"))

# Compute the sum
sum = n * (n + 1) / 2

# Display the result
print("The sum of the first positive integers between 1 and", n, "is", int(sum))
