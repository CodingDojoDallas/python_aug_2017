class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.displayAll()

    def displayAll(self):
        if self.price >= 10000:
            self.price += self.price * 15/100
        else:
            self.price += self.price * 12/100
            
        print "The car's price:{}, the top speed is:{}, it's fuel is:{}, and the mileage is:{}".format(self.price,self.speed,self.fuel,self.mileage)

Car1 = Car(5000, 80, "unleaded", 50)
Car2 = Car(8000, 90, "unleaded", 45)
Car3 = Car(10000, 120, "unleaded", 40)
Car4 = Car(15000, 120, "unleaded", 35)
Car5 = Car(20000, 125, "premium", 25)
Car6 = Car(25000, 150, "premium", 15)


# Car1.displayAll()
#         alllow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

# Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.