from bicycles2 import Bicycle, Wheels, Frames, Customer, BikeShop

if __name__ == "__main__":
    
    wheel_1 = Wheels('All Terrain', 1.21, 45.0)
    wheel_2 = Wheels('Off Road', 1.22, 68.0)
    wheel_3 = Wheels('Street', 0.58, 120.0)
    
    frame_1 = Frames('Aluminum', 19, 200.0)
    frame_2 = Frames('Steel', 55, 75.0)
    frame_3 = Frames('Carbon Fiber', 15, 700.0)
    
    bike_1 = Bicycle(wheel_1, frame_2)
    bike_2 = Bicycle(wheel_3, frame_3)
    bike_3 = Bicycle(wheel_2, frame_1)
    
    person_1 = Customer('Jhon Doe', 200.00)
    person_2 = Customer('Gemma Cain', 500.00)
    person_3 = Customer('Marco Reus', 1000.00)
    
    shop_inventory = {
        'Palmentto': (bike_1, 5),
        'XC700': (bike_2, 5),
        'Marina': (bike_3, 5)
    }
    
    shop = BikeShop('Cycles', shop_inventory)
    
    bike_1.bike_price()
    bike_2.bike_price()
    bike_3.bike_price()
    person_1.affordable_bikes(shop)
    person_2.affordable_bikes(shop)
    person_3.affordable_bikes(shop)
    shop.print_inventory()
    person_1.buy('Palmentto', shop)
    person_2.buy('Marina', shop)
    person_3.buy('XC700', shop)
    shop.print_inventory()