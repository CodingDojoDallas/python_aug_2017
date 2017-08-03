class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print "the bike's price:{}, max speed:{}, and total miles are:{}".format(self.price,self.max_speed,self.miles)
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5
            return self
        else:
            self.miles -= 0
            print "Can't reverse anymore."
            return self





BMX = Bike(500, 15)
Mountain = Bike(800, 30)
Road = Bike(1000, 40)
# print BMX.price
# print Mountain.max_speed
# print Road.price
# BMX.reverse()

# BMX.ride().ride().ride().reverse().displayInfo()
# Mountain.ride().ride().reverse().reverse().displayInfo()
Road.reverse().reverse().reverse().displayInfo()
