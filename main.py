from bicycles import Bicycle, Customer, BikeShop

if __name__ == "__main__":
    bike_1 = Bicycle('Schwinn', 'Protocol 1.0', '41 lbs.', 320.0)
    bike_2 = Bicycle('Schwinn', 'Ladies Perla', '42 lbs.', 160.0)
    bike_3 = Bicycle('Columbia', 'Palmetto', '38 lbs.', 140.0)
    bike_4 = Bicycle('Cyrusher', 'XC700', '32 lbs.', 680.0)
    bike_5 = Bicycle('Fito', 'Marina', '33 lbs.', 200.0)
    bike_6 = Bicycle('Huffy', 'Fresno', '42 lbs.', 190.0)
    
    person_1 = Customer('Jhon Doe', 200.00)
    person_2 = Customer('Gemma Cain', 500.00)
    person_3 = Customer('Marco Reus', 1000.00)
    
    shop_inventory = {
        'Protocol 1.0': (bike_1, 5),
        'Ladies Perla': (bike_2, 5),
        'Palmentto': (bike_3, 5),
        'XC700': (bike_4, 5),
        'Marina': (bike_5, 5),
        'Fresno': (bike_6, 5)
    }
    
    shop = BikeShop('Cycles', shop_inventory)
    
    person_1.affordable_bikes(shop)
    person_2.affordable_bikes(shop)
    person_3.affordable_bikes(shop)
    shop.print_inventory()
    person_1.buy('Palmentto', shop)
    person_2.buy('Protocol 1.0', shop)
    person_3.buy('XC700', shop)
    shop.print_inventory()