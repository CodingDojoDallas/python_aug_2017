# need to go back and figure out tax
class Product(object):
	def __init__(self, name, price, brand, weight, cost):
		self.name = name
		self.price = price
		self.brand = brand
		self.weight = weight
		self.cost = cost
		self.status = 'for sale'
		self.displayInfo()

	def sell(self):
		self.status = 'sold'
		return self

	def add_tax(self, tax):
		self.price = self.price + self.price * tax
		print self.price
		return self

	def returns(self, reason):
		if (reason == 'defective'):
			self.status = 'defective'
			self.price = 0
		elif (reason == 'in box'):
			self.status = "for sale"
		return self

	def displayInfo(self):
		print 'Name: ' + str(self.name)
		print 'Price: $' + str(self.price)
		print 'Brand: ' + str(self.brand)
		print 'Weight: ' + str(self.weight) + 'lbs.'
		print 'Cost: $' + str(self.cost)
		print 'Status: ' + str(self.status)

product1 = Product('banana', .50, 'Chaquita', .1, .25)
product2 = Product('apple', 1.50, 'Dole', .2, .75)
product3 = Product('avacado', 2.50, 'Haas', .3, 1.00)
product4 = Product('green pepper', 1.75, 'Dole', .3, .95)
