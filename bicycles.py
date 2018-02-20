class Bicycle(object):
    
    def __init__(self, manufacturer, model, weight, cost):
        self.manufacturer = manufacturer
        self.model = model
        self.weight = weight
        self.cost = cost
        
    def bike(self):
        return '{} {}'.format(self.manufacturer, self.model)
        
bike_1 = Bicycle('Schwinn', 'Protocol 1.0', '41 lbs.', 320.00)
bike_2 = Bicycle('Schwinn', 'Ladies Perla', '42 lbs.', 160.00)
bike_3 = Bicycle('Columbia', 'Palmetto', '38 lbs.', 140.00)
bike_4 = Bicycle('Cyrusher', 'XC700', '32 lbs.', 680.00)
bike_5 = Bicycle('Fito', 'Marina', '33 lbs.', 200.00)
bike_6 = Bicycle('Huffy', 'Fresno', '42 lbs.', 190.00)

class Customer(object):
    
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        
person_1 = Customer('Jhon Doe', 200.00)
person_2 = Customer('Jemma Cain', 500.00)
person_3 = Customer('Marco Reus', 1000.00)

class Bike_Shop(object):
    
    def __init__(self, name):
        self.name = name

    def inventory(self):
        for bikes, stock in supply.items():
            print(bikes.bike(), ':', stock)
            
    def sell(self, bikes):
        for bikes, stock in supply.items():
            if bikes in supply.items():
                stock -= 1
        return supply.items()
        
    # def profit(self):
    #     for bikes sold
    #         profit = cost * 0.2
            
shop = Bike_Shop('Cycles')

supply = {
    bike_1: 1,
    bike_2: 1,
    bike_3: 1,
    bike_4: 1,
    bike_5: 1,
    bike_6: 1,
}

if __name__ == "__main__":
    print(shop.inventory())
    shop.sell(bike_1)
    print(shop.inventory())