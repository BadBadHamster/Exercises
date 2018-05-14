# Exercise 6 - Tax and Tip

# input from the customer
sidedish = input("Enter the name of the side dish \n")
var1 = float(input("Enter the price for the side dish in zloty \n"))
maindish = input("Enter the name of the main dish \n")
var2 = float(input("Enter the price for the main dish in zloty \n"))
dessert = input("Enter the name of the dessert \n")
var3 = float(input("Enter the price for the dessert in zloty \n"))

# tip and tax calculation
total = var1 + var2 + var3
tip = 0.18 * total
tax = 0.23 * total

# bill
print()
print(sidedish, round(var1, 2), "zł")
print(maindish, round(var2, 2), "zł")
print(dessert, round(var3, 2), "zł")
print("18% Tip included", round(tip, 2), "zł")
print("23% tax included", round(tax, 2), "zł")
print("Total", round(total + tip + tax), "zł")
