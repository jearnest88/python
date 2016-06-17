import random
class Animal(object):
    def __init__(self):
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print 'My health is at: ' + str(self.health)
        return self

class Dog(Animal):
    def __init__(self):
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self):
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
animal1 = Animal()
animal1.walk().walk().walk().run().run().displayHealth()

dog1 = Dog()
dog1.walk().walk().walk().run().run().pet().displayHealth()

dragon1 = Dragon()
dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()
