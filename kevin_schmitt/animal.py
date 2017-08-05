class Animal(object):
    def __init__(self, name, health):
        print "I'm creating an animal."
        self.name = name
        self.health = health

    def walk(self):
        print 'walking'
        self.health -= 1
        return self
    def run(self):
        print 'running'
        self.health -= 5
        return self
    def display_health(self):
        print "This animal's health is {}.".format(self.health)
        return self
    # def instance(self):
    #     self.walk
    #     self.run
    #     self.run
    #     self.run
    #     print "Now the animal has {} for health.".format(self.health)

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()
        self.health = 150
    def pet(self):
        self.health +=5

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
    def fly(self):
        self.health -= 10
    def healthinfo(self):
        print "I'm a Dragon!"
        super(Dragon, self).display_health()
        return self



crow = Animal('Crow',80)
cat = Animal('Cat',70)
bird = Animal('Tweety',20)
dragon = Dragon('duke',199)

crow.walk().walk().walk().run().run().display_health()
dragon.healthinfo()