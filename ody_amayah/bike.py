class bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    # bike1 = bike(3000, "250mph")
    # bike2 = bike(5000, "500mph")

    def displayInfo(self): 
        print 'price is $:' + str(self.price)
        print 'maximum speed is:' + str(self.max_speed) + 'mph'
        print 'Total miles is: ' + str(self.miles) + 'miles'
        return self


    def ride(self):
        print 'driving'
        self.miles += 25
        return self


    def reverse(self):
         print 'reversing'
         if self.miles >= 10:
             self.miles -= 10
             return self



bike1 = bike(100, 15)
bike1.ride()
bike1.displayInfo()
bike1.reverse()














        



