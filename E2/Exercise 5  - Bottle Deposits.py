# Exercise 5 - Bottle Deposits

# input from the customer
var1 = int(input("Enter a number of drink containers holding one litre or less \n"))
var2 = int(input("Enter a number of drink containers holding more than one litre \n"))

# calculation of deposit
depo1 = var1 * 0.10
depo2 = var2 * 0.25
total = depo1 + depo2

# outout
print("Refund for returning drink containers holding one litre or less is", round(depo1, 2), "$")
print("Refund for returning drink containers holding more than litre is", round(depo2, 2), "$")
print("Total refund is", round(total, 2), "$")
