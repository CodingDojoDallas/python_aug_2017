class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def  displayInfo(self):
        print 'Price is: $ ' + str(self.price)
        print 'Max Speed is: ' + str(self.max_speed) + 'mph'
        print 'Total Miles is: ' + str(self.miles) + 'miles'
        return self

    def drive(self):
        print 'Driving'
        self.miles += 10
        return self

    def reverse(self):
        print 'Reversing'
        if self.miles >= 5:
           miles -= 5    
           return self
        else:
            self.miles -= 0
            print "Can't reverse anymore"
            return self
             
  
CRX = Bike(220, 9)
Suzuki = Bike(120, 15)
Fuji = Bike(180, 12)

print CRX.price
print Suzuki.max_speed
print Fuji.price       

CRX.reverse()
Suzuki.drive().drive().reverse()
CRX.drive().drive().reverse().displayInfo()
Fuji.ride().ride().reverse().reverse().displayInfo()
Road.reverse().reverse().reverse().displayInfo()