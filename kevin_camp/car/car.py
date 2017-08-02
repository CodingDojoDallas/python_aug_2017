class Car(object):

	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if price > 10000:
			self.tax = .15
		else:
			self.tax = .12
		self.display_all()

	def display_all(self):
		print 'Price: $' + str(self.price)
		print 'Speed:' + str(self.speed) + 'mph'
		print 'Fuel:' + str(self.fuel)
		print 'Mileage:' + str(self.mileage) + 'mpg'
		print 'Tax:' + str(self.tax)

car1 = Car(5000, 75, 'Full', 15)
car2 = Car(7500, 100, 'Not Full', 105)
car3 = Car(12500, 15, 'Kinda of Full', 95)
car4 = Car(2000, 25, 'Full', 25)
car5 = Car(9500, 45, 'Empty', 25)
car6 = Car(500000, 150, 'Empty', 15)
