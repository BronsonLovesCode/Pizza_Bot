# List of pizza names
pizza_names = ['Margherita','Pepperoni','Hawaiian','Cheese','Italian','Veggie','Vegan',
               'Chicken Deluxe','Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe']

# List of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

# List to store ordered pizzas
order_list = []

# List to store  pizza prices
order_cost = []

#List to store order cost

def menu():
    number_pizzas = 12

    for count in range (number_pizzas):
        print("{} {} ${:.2f}" .format(count+1,pizza_names[count],pizza_prices[count]))

menu()

# Ask for total number of pizzas for order
num_pizzas = 0

num_pizzas = int(input("*** How many pizzas do you want to order? *** "))

print(num_pizzas)

# Choose pizza from menu
print("*** Please choose your pizza(s) by entering the number from the menu. *** ")
for item in range(num_pizzas):
    while num_pizzas > 0:
        pizza_ordered = int(input())
        order_list.append(pizza_names[pizza_ordered])
        order_cost.append(pizza_prices[pizza_ordered])
        num_pizzas = num_pizzas-1

#print(order_list)
#print(order_cost)




# Countdown until all pizzas are ordered




# Print order