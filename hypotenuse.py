import math
# user input of the shorter sides 
a = int(input("Enter a length: "))
b = int(input("Enter another length: "))

# function to calculate hypotenuse 
def pythagorean_theorem(a, b): 
    c = math.sqrt(a**2 + b**2)
    c = str(c)
    return c 

# printing length of hypotenuse 
print("The length of the hypotenuse is:" + " " + pythagorean_theorem(a, b) + " " + "cm.")