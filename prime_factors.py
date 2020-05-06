import math

# getting user input for integer 
integer = int(input("Enter an integer (2 or greater): "))

# determining if it is in the correct range (=>2)
if integer < 2:
    print("Incorrect value. Try again.")
    exit()
else: 
    number = integer
    print("The prime factors of" + " " + str(number) + " " + "are:" )

# the process of factorization 
factor = 2
while factor <= number: 
    if math.remainder(number, factor) == 0:
        print(factor)
        number = number // factor 
    else: 
        factor = factor + 1