class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = 0

        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
            



    def display_all(self):
        print 'price is ${}'.format(self.price + self.price * self.tax)
        print 'maximum speed is:' + str(self.speed) + 'mph'
        print 'fuel is on:' + str(self.fuel)
        print 'total mileage is:' + str(self.mileage) + 'mpg'

  

car1 = car(2000, "35mph", "full", "15mpg")    
car2 = car(2000, "5mph", "not full", "105mpg")
car3 = car(2000, "15mph", "Kind of full", "95mpg")
car4 = car(2000, "25mph", "full", "25mpg")
car5 = car(2000, "45mph", "not full", "25mpg")
car6 = car(2000, "35mph", "not full", "15mpg")

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
