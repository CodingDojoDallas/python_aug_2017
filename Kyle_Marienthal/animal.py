class Animal(object):
    def __init__(self,name):
        self.name = name
        self.health = 50

    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.health

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        
        health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name)
        health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_Health(Animal, self):
        print "{}, I'm a Dragon"
        return self


# parrot = Animal('max')
# parrot.walk().walk().walk().run().run().display_health()

# pit = Dog("max")
# pit.walk().walk().walk().run().run().pet().display_health()

