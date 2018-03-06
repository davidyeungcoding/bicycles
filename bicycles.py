class Bicycle(object):
    
    def __init__(self, manufacturer, model, weight, cost):
        self.manufacturer = manufacturer
        self.model = model
        self.weight = weight
        self.cost = cost
        
class Customer(object):
    
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        
    def affordable_bikes(self, bike_shop):
        """Provides a list of bikes that the customer can afford"""
        print(self.name)
        print('Here are the bikes that fall within your budget:')
        for bike_name, stock in bike_shop.inventory.items():
            if stock[0].cost <= self.cash:
                print(bike_name)
        
    def buy(self, bike_model, bike_shop):
        """Goes through the transaction process"""
        print(self.name)
        print("I'd like to purchase the {}.".format(bike_model))
        sell_price = bike_shop.sell(bike_model)
        print('Total comes to ${}'.format(sell_price))
        self.cash = self.cash - sell_price
        print("Here's your change: ${}".format(self.cash))

class BikeShop(object):
    
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        self.profit = 0
        

    def print_inventory(self):
        """Prints the inventory for the store"""
        print('Inventory:')
        for bike_name, stock in self.inventory.items():
            print(bike_name, ':', stock[1])
        print('Total Profit = ${}'.format(self.profit))
            
    def sell(self, bike_model):
        """Subtracts stock and calculates profit"""
        bike, stock = self.inventory[bike_model]
        self.inventory[bike_model] = (bike, stock - 1)
        self.profit += 0.2 * bike.cost
        return bike.cost