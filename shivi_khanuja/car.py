class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000 :
            self.tax = 0.15
        else:
            self.tax = 0.12            


    def display(self):
        print "Price is: ${} ".format(self.price + self.price * self.tax)
        print 'Max Speed is: ' + str(self.speed) + 'mph'
        print 'Mileage is: ' + str(self.mileage) + 'miles'
        return self

    def gas(self):
      if self.fuel == 10:
         print "Fuel is: {} gal ".format(self.fuel) +  "Kind of Full"

      elif self.fuel == 15:
         print "Fuel is: {} gal ".format(self.fuel) +  "Full"

      elif self.fuel == 5:
         print "Fuel is: {} gal ".format(self.fuel) +  "Not Full"
      else:       
        print "Fuel is: {} gal ".format(self.fuel) +  "Empty"
        return self

    
             

car1 = Car(12000, 65, 10, 10)
car2 = Car(9000, 55, 5, 12)
car3 = Car(15000, 55, 0, 16)
car4 = Car(14500, 65, 15, 13)
car5 = Car(7000, 30, 10, 15)
car6 = Car(17000, 75, 15, 14)
car1.display().gas()
print "  "
car2.display().gas()
print "  "
car3.display().gas()
print "  "
car4.display().gas()
print "  "
car6.display().gas()
print "  "
car5.display().gas()
print "  "