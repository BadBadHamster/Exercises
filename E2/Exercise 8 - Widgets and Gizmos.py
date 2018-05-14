# Exercise 8 - Widgets and Gizmos

# Compute total weight of widgets and gizmos according to customer order

# Read input from customer
nW = int(input("Enter a quantity of Widgets you want to order \n"))
nG = int(input("Enter a quantity of Gizmos you want to order \n"))

# Weight calculation
wW = 75  # grams
wG = 112  # grams

twW = nW * wW  # total weight of Widgets
twG = nG * wG  # total weight of Gizmos
total = twW + twG

# Results
print("Total weight of ordered Widgets and Gizmos is", total, "grams")
