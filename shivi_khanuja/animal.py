class Animal(object):
    def __init__(self, name):
        self.health = 100
        self.name = name

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print 'My name is: ' + self.name
        print 'I have: ' + str(self.health) + ' health'

class Monkey(Animal):
    def __init__(self,name):
        super(Monkey, self).__init__(name)
        self.health = 150
        
    def pet(self):
        print "This is a Monkey"
        self.health += 5
        return self        

monkey= Monkey('Tom')
monkey.walk().walk().walk().run().run().pet().displayHealth()

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
        self.health = 150
        
    def pet(self):
        print "This is a Dog"
        self.health += 5
        return self

dog = Dog('Dony')
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 195

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "This is a dragon"
        super(Dragon, self).displayHealth()

dragon = Dragon('Pete')
dragon.fly().displayHealth()