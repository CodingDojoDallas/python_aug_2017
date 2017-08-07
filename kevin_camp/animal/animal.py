#create Parent class
class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print 'Hi, my name is ' + self.name
		print 'My health is ' + str(self.health)
		return self

#test case should = (100-9)=91
Animal("Pokey the Pachyderm").walk().walk().walk().walk().run().displayHealth()
print Animal

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150

	def pet(self):
		self.health += 5
		return self

#different syntax from example above health should be 151
dog = Dog('Faith')
dog.walk().walk().walk().walk().pet().displayHealth()

class Dragon(Animal):
	def __init__(self, name): #different syntax than above
		super(Dragon, self).__init__(name)
		self.health = 500

	def fly(self):
		self.health -= 10
		return self

	def damage(self):
		self.health -= 100
		return self

	def displayHealth(self):
		print 'Hey Dragonbourne, I am a Dragon'
		super(Dragon, self).displayHealth()
		return self

#test dragon
dragon = Dragon('Paarthunax')
dragon.fly().damage().displayHealth()
