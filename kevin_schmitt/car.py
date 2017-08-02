class car(object):
    def __init__(self, name, price, speed, fuel, mileage):        
        self.name = name
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        print type(self.price)
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12

    def display_all(self):
        print 'Name: {} Price: {} Speed: {} Fuel: {} Mileage: {} Tax: {}'.format(self.name,self.price,self.speed,self.fuel,self.mileage,self.tax)
        
        


honda = car('civic',2000,'35mph','full','15mpg')
minicoop = car('mini cooper',2400,'5mph','not full','105mpg')
bmw = car('bmw',21000,'40mph','empty','24mpg')
honda.display_all()
minicoop.display_all()
bmw.display_all()