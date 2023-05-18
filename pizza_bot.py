# Pizza bot program
import random
from random import randint




# List of random names
names = ["Bronson", "Adam", "Alain", "Ethan", "Eardwulf", "Santiago", "Daniel", "Dannell", "Luka", "Jason"]




# Customer details dictionary
customer_details = {}




# Validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("*** This cannot be blank. ***")




# Welcome message with random name
def welcome():
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message
    Parameters: None
    Returns: None

    '''
    num = randint(0,9)
    name = (names[num])
    print("*** welcome to Dream Pizzas! ***")
    print("*** My name is",name, "***")
    print("*** I will be here to help you order your delicous Dream Pizza ***")




    # Menu for pickup or delivery
def order_type():
    print ("*** Is your order for pickup or delivery? ***")
    print ("*** For delivery, enter 1. *** ")
    print ("*** For pickup, enter 2. *** ")
    while True:
        try:
                delivery = int(input("*** Please enter a number. *** "))
                if delivery >= 1 and delivery <= 2:
                    if delivery == 1:
                            print ("Delivery")
                            break
                    elif delivery == 2:
                            print ("Pickup")
                            pickup()
                            break
                else:
                    print ("*** The number must be 1 or 2. *** ")
        except ValueError:
                print ("*** That was not a valid input... *** ")
                print ("*** Please enter 1 or 2. *** ")




# Pick up information - name and phone number
def pickup():
    question = ("*** Please enter your name. *** ")
    customer_details['name'] = not_blank(question)
    #print (customer_details['name'])

    question = ("*** Please enter your phone number. *** ")
    customer_details['phone'] = not_blank(question)
    #print (customer_details['phone'])
    print(customer_details)




# Delivery information - name address and phone





# Choose total Number of Pizzas - max 5






# Pizza menu






# Pizza order - from menu - print each pizza ordered with cast





# Print order out - including if order is delivery or pick up and names and price of each pizza - totaql cost including any delivery charge




# Ability to cancel or proceed with order




# Option for new order or to exit






# Main Fuction
def main():
    '''
    Purpose: To run all functions
    a welcome message
    Parameters: None
    Returns: None

    '''
    welcome()
    order_type()

main()