# Represents an abstract bike
class Bike(object):
    def __init__(self, name, weight, cost):
        # Initializes the bike's name, weight, cost and price
        self.name = name
        self.weight = weight
        self.cost = cost
        self.price = cost  
# An abstract bike shop
class BikeShop(object):
    profit = 0
    def __init__(self, name, margin):
        # Initialize the shop's name, marging and (empty) inventory
        self.name = name
        self.margin = margin
        self.inventory = []
    def add_inventory(self, bike):
        # Add a bike to the inventory, changing its price to reflect the
        # margin
        bike.price = bike.cost * (1 + self.margin)
        self.inventory.append(bike)
class Customer(object):
    def __init__(self,name,fund,own_bike):
        #Initialize the customer object
        self.name
        self.fund
        own_bike = True 
# Create a series of different types of bike
bikes = {}
bikes["Mountain Bike"] = Bike("Mountie", 10, 100)
bikes["Road Bike"] = Bike("Roadie", 8, 150)
bikes["Rack Bike"] = Bike("Racer", 7, 200)
# Create a shop
shop = BikeShop("Joe's Bikes", 0.2)
# Add each bike to the shop's inventory
for bike_type in bikes:
    shop.add_inventory(bikes[bike_type])
customers = {}
customers["Cust1"] = Customer("Dave",200,False)
customers["Cust2"] = Customer("Han",500,False)
customers["Cust3"] = Customer("Ash",1000,False)
for each cust in customers:
    if customers[key] > shop.inventory

