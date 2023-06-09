# Pizza bot program
# 18/05/23
# Bugs - Phone number input allows letters
#      - Name input allows numbers


import sys
import random
from random import randint



# List of random names
names = ["Bronson", "Adam", "Alain", "Ethan", "Eardwulf", "Santiago", "Daniel", "Dannell", "Luka", "Jason"]



# List of pizza names
pizza_names = ['Margherita','Pepperoni','Hawaiian','Cheese','Italian','Veggie','Vegan',
               'Chicken Deluxe','Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe']



# List of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]



# List to store ordered pizzas
order_list = []



# List to store pizza prices
order_cost = []



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
    del_pick = ""
    print ("*** Is your order for pickup or delivery? ***")
    print ("*** For delivery, enter 1. *** ")
    print ("*** For pickup, enter 2. *** ")
    while True:
        try:
                delivery = int(input("*** Please enter a number. *** "))
                if delivery >= 1 and delivery <= 2:
                    if delivery == 1:
                            print ("Delivery")
                            #order_list.append("*** Delivery Charge ***")
                            #order_cost.append(5)
                            delivery_info()
                            del_pick = "delivery"
                            break
                    elif delivery == 2:
                            print ("Pickup")
                            pickup_info()
                            del_pick = "pickup"
                            break
                else:
                    print ("*** The number must be 1 or 2. *** ")
        except ValueError:
                print ("*** That was not a valid input... *** ")
                print ("*** Please enter 1 or 2. *** ")
    return del_pick



# Pick up information - name and phone number
def pickup_info():
    question = ("*** Please enter your name. *** ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])

    question = ("*** Please enter your phone number. *** ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])
    print(customer_details)



# Delivery information - name address and phone
def delivery_info():
    question = ("*** Please enter your name. *** ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])

    question = ("*** Please enter your phone number. *** ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])

    question = ("*** Please enter your house number. *** ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])

    question = ("*** Please enter your street name. *** ")
    customer_details['street'] = not_blank(question)
    print (customer_details['street'])

    question = ("*** Please enter your suburb. *** ")
    customer_details['suburb'] = not_blank(question)
    print (customer_details['suburb'])
    print (customer_details)

# Pizza Menu
def menu():
    number_pizzas = 12
    for count in range (number_pizzas):
        print("{} {} ${:.2f}" .format(count+1,pizza_names[count],pizza_prices[count]))



# Choose total Number of Pizzas - max 5
# Pizza order - from menu - print each pizza ordered with cast
def order_pizza():
# Ask for total number of pizzas for order
    num_pizzas = 0
    while True:
        try:
            num_pizzas = int(input("*** How many pizzas do you want to order? *** "))
            if num_pizzas >= 1 and num_pizzas <= 5:
                break
            else:
                print("*** Your order must be between 1 and 5. ***")
        except ValueError:
            print("*** That is not a valid number. ***")
            print("*** Please enter a number between 1 and 5. *** ")
    # Choose pizza from menu
    for item in range(num_pizzas):
        while num_pizzas > 0:
            while True:
                try:
                    pizza_ordered = int(input("*** Please choose your pizza(s) by entering the number from the menu. *** "))
                    if pizza_ordered >= 1 and pizza_ordered <= 12:
                        break
                    else:
                        print("*** Your order must be between 1 and 12. ***")
                except ValueError:
                    print("*** That is not a valid number. ***")
                    print("*** Please enter a number between 1 and 12. *** ")
            pizza_ordered = pizza_ordered -1
            order_list.append(pizza_names[pizza_ordered])
            order_cost.append(pizza_prices[pizza_ordered])
            print("{} ${:.2f}" .format(pizza_names[pizza_ordered],pizza_prices[pizza_ordered]))
            num_pizzas = num_pizzas -1



# Print order out - including if order is delivery or pick up and names and price of each pizza - totaql cost including any delivery charge
def print_order(del_pick):
    total_cost = sum(order_cost)
    print()
    print("*** Customer Details ***")
    if del_pick == "delivery":
        print("Your order is for delivery. A $5.00 dollar delivery charge applies.")
        total_cost = total_cost + 5
        print(f"Name: {customer_details['name']} \nPhone number: {customer_details['phone']} \nAddress: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    elif del_pick == "pickup":
        print("Your order is for pickup.")
        print(f"Name: {customer_details['name']} \nPhone number: {customer_details['phone']}")
    print()
    print("*** Order Details ***")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("*** Total Order Cost ***")
    print(f"${total_cost:.2f}")
    print()



# Ability to cancel or proceed with order
def confirm_cancel():
    print ("*** Please confirm your order. ***")
    print ("*** To confirm order, enter 1. ***")
    print ("*** To cancel order, enter 2. ***")

    while True:
        try:
                confirm = int(input("*** Please enter a number. *** "))
                if confirm >= 1 and confirm <= 2:
                    if confirm == 1:
                            print ()
                            print ("*** Order confirmed ***")
                            print ()
                            print ("Your order has been sent to our kitchen to be prepared,")
                            print ("your pizza will be with you shortly!")
                            print ()
                            break

                    elif confirm == 2:
                            print ()
                            print ("*** Order cancelled ***")
                            print ()
                            print ("You can restart your order or exit the BOT.")
                            print ()
                            break
                else:
                    print ("*** The number must be 1 or 2. *** ")
        except ValueError:
                print ("*** That was not a valid input... *** ")
                print ("*** Please enter 1 or 2. *** ")



# Option for new order or to exit
def new_exit():
    print ("*** Do you wish to start another order or exit? ***")
    print ("*** To start another order, enter 1. ***")
    print ("*** To exit the BOT, enter 2. ***")

    while True:
        try:
                confirm = int(input("*** Please enter a number. *** "))
                if confirm >= 1 and confirm <= 2:
                    if confirm == 1:
                            print ("*** New Order ***")
                            order_list.clear()
                            order_cost.clear()
                            customer_details.clear()
                            main()
                            break

                    elif confirm == 2:
                            print ("*** Exiting BOT ***")
                            order_list.clear()
                            order_cost.clear()
                            customer_details.clear()
                            sys.exit()                       
                            break
                else:
                    print ("*** The number must be 1 or 2. *** ")
        except ValueError:
                print ("*** That was not a valid input... *** ")
                print ("*** Please enter 1 or 2. *** ")



# Main Fuction
def main():
    '''
    Purpose: To run all functions
    a welcome message
    Parameters: None
    Returns: None

    '''
    welcome()
    del_pick = order_type()
    menu()
    order_pizza()
    print_order(del_pick)
    confirm_cancel()
    new_exit()

main()