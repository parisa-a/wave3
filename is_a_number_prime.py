import math 
# getting user input 
number = int(input("Please input a positive number: "))

# making sure prime number can be found
if number < 2:
    print("Incorrect value. Try again.")
    exit()

# function to determine if it's a prime number 
def prime_factorization(number):
    if number == 2 or number == 3:
            output = (str(number) + " " + "is a prime number.")
            return (output)
    for factor in range (2, number - 1):
        if (number % factor) == 0: 
            output = (str(number) + " " + "is not a prime number.")
            break
        else: 
            output = (str(number) + " " + "is a prime number.")
    return (output)

print(prime_factorization(number))