# user input of number of items purchased
items = int(input("Please enter amount of items purchased: "))

# function to calculate charge
def shipping_charge(items): 
    charge = 10.95 + (2.95 * (items - 1))
    return charge

# %.2f adds the second decimal place if it isn't there 
# % is replaced with the shipping charge function, .2 is the number of decimal places, and f means float
print("Your shipping charge is $%.2f" % shipping_charge(items))