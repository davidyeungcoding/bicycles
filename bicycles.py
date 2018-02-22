class Bicycle(object):
    
    def __init__(self, manufacturer, model, weight, cost):
        self.manufacturer = manufacturer
        self.model = model
        self.weight = weight
        self.cost = cost
        
    # def bike(self):
    #     """Prints manufacturer and bike name together"""
    #     return '{} {}'.format(self.manufacturer, self.model)
        
class Customer(object):
    
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

class BikeShop(object):
    
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        self.profit = 0

    # def inventory(self):
    #     """Prints the inventory for the store"""
    #     for bikes, stock in supply.items():
    #         print(bikes.bike(), ':', stock)
            
    def sell(self, profit):
        """Adds sold bikes to the sold_bikes list"""
        self.profit = 0.2 * cost

if __name__ == "__main__":
    bike_1 = Bicycle('Schwinn', 'Protocol 1.0', '41 lbs.', 320.0)
    bike_2 = Bicycle('Schwinn', 'Ladies Perla', '42 lbs.', 160.0)
    bike_3 = Bicycle('Columbia', 'Palmetto', '38 lbs.', 140.0)
    bike_4 = Bicycle('Cyrusher', 'XC700', '32 lbs.', 680.0)
    bike_5 = Bicycle('Fito', 'Marina', '33 lbs.', 200.0)
    bike_6 = Bicycle('Huffy', 'Fresno', '42 lbs.', 190.0)
    
    person_1 = Customer('Jhon Doe', 200.00)
    person_2 = Customer('Jemma Cain', 500.00)
    person_3 = Customer('Marco Reus', 1000.00)
    
    shop_inventory = {
        'Protocol 1.0': (bike_1, 5),
        'Ladies Perla': (bike_2, 5),
        'Palmentto': (bike_3, 5),
        'XC700': (bike_4, 5),
        'Marina': (bike_5, 5),
        'Fresno': (bike_6, 5),
    }
    
    shop = BikeShop('Cycles', shop_inventory)
    
    print(shop.inventory)