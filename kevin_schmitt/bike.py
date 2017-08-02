class Bike(object):
    def __init__(self, name, price, max_speed, miles):
        print 'I am creating a Bike'
        self.name = name
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print 'My bike"s name is {}. Price is {}. Maximum speed is {}. And total miles is {}'.format(self.name,self.price,self.max_speed,self.miles)
    def ride(self):
        print "riding!..."
        self.miles += 10
        print "I've riden {} on this cool bike.".format(self.miles)
        return self
    def reverse(self):
        print 'Reversing!...'
        if self.miles >= 5:
            self.miles -= 5
            print 'Now i have ridden {} miles since i have gone backwards!'.format(self.miles)
        return self
    
bike1 = Bike('Schwinn', '300','32', '500')
bike2 = Bike('Huffy',  '201','28','600')
print bike1.max_speed
print bike2.price
bike2.displayinfo()
bike1.ride()
bike1.reverse()