# Exercise 3 Area of a Room

L = input("Please input lenght of a room in meters\n")  # string from user
W = input("Please input width of a room in meters\n")  # string from user
lenght = int(L)  # convertion of string input from the user to the number int() or float ()
width = int(W)  # convertion of string input from the user to the number int() or float ()
area = lenght * width
print("The area of the room is equal", area, "cubic meters")
