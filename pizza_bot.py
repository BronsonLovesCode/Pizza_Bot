# Pizza bot program
import random
from random import randint

# List of random names
names = ["Bronson", "Adam", "Alain", "Ethan", "Eardwulf", "Santiago", "Daniel", "Dannell", "Luka", "Jason"]

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






# Pick up information - name and phone number






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

main()