# Program name: LEWIS_BRENT_M08_FP
# Author: Brent Lewis
# Date: 5/10/2022
# Summary: Create a pizza ordering app
# Variables:
#   availPizzas: available pizzas to order (str) list
#   pizPrice: prices for pizzas (int) array
#   pizza: what pizza the user wants (str)

# Making the lists
availPizzas = ['pepperoni', 'sausage', 'cheese']
pizPrice = {'pepperoni': 5, 'sausage': 5, 'cheese': 3}

# Displaying the menu
def showMenu():
    print("Available pizzas:\n")
    print(*availPizzas, sep = ', ')
    print('\n\n')

# Greeting the user, getting info on what the user wants and displaying the order
def takeOrderInput():
    print("Hi, welcome to our text based pizza ordering app.")
    while ordering:
        showMenu()
        pizza = input("Please choose a pizza: ").lower()


    return pizza

class Order:
    def __init__(self):
        pizza = takeOrderInput()
        self.pizza = pizza
        self.pizzaPrice = pizPrice[pizza]
        self.total = self.pizzaPrice

# Asking the user if they want to order and if they would like to order again
orders = []
while choice:
    newOrder = Order()
    orders.append(newOrder)
    newChoice = input("Would you like to order again? (Y/N): ").upper()
    if (newChoice) == 'N':
        break

# Displaying total of order and prompting the user to provide name, address and phone number
total = 0
for order in orders:
    total += order.total

print("Total: ", "${:.2f}".format(total))
print("Please provide us with your name, address and phone number for delivery.")

class Customer():

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getPhone(self):
        return self.phone

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setPhone(self, phone):
        self.phone = phone

def info():
    myName = input("Enter your name: ")
    myAddress = input("Enter your address: ")
    myPhone = input("Enter your phone number: ")

    # Create an instance of the customer
    myCustRecord = Customer(myName, myAddress, myPhone)

    # Display customer info
    print()
    print("Name: " + myCustRecord.getName())
    print("Address: " + myCustRecord.getAddress())
    print("Phone: " + myCustRecord.getPhone())
    print("Thanks for your order, We'll have your order out ASAP! If we have a problem, we'll call the number provided.")

info()

