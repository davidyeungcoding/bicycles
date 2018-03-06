class Wheels(object):
    
    def __init__(self, wheel_model, wheel_weight, wheel_cost):
        self.wheel_model = wheel_model
        self.wheel_weight = wheel_weight
        self.wheel_cost = wheel_cost
    
class Frames(object):
    
    def __init__(self, frame_material, frame_weight, frame_cost):
        self.frame_material = frame_material
        self.frame_weight = frame_weight
        self.frame_cost = frame_cost

class Bicycle(object):
    
    def __init__(self, wheels, frame):
        self.wheels = wheels
        self.frame = frame
        self.weight = self.bike_weight
        self.cost = self.bike_price
        
    def bike_weight(self):
        """Calculates the total weight of the bike"""
        self.weight = self.wheels.wheel_weight * 2.0 + self.frame.frame_weight
        return self.weight
        
    def bike_price(self):
        """Calculates the cost of the bike based on the fame and wheels"""
        self.cost = self.wheels.wheel_cost * 2.0 + self.frame.frame_cost
        return self.cost

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