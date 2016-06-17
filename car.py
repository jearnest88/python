class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def tax(self):
        if self.price > 10000:
            self.tax = 0.15
            return (self.tax)
        else:
            self.tax = 0.12
            return (self.tax)

    def displayInfo(self):
        print 'Price: ' + str(self.price)
        print 'Speed: ' + str(self.speed) + 'mph'
        print 'Fuel: ' + str(self.fuel)
        print 'Mileage: ' + str(self.mileage) + 'mpg'
        print 'Tax: ' + str(self.tax) + '\n'

car1 = Car(11000, 60, 'full', 30)
car1.tax()
car1.displayInfo()

car2 = Car(2000, 35, 'Not Full', 40)
car2.tax()
car2.displayInfo()

car3 = Car(8000, 45, 'Full', 90)
car3.tax()
car3.displayInfo()

car4 = Car(12000, 85, 'Not Full', 90)
car4.tax()
car4.displayInfo()

car5 = Car(3000, 15, 'Full', 05)
car5.tax()
car5.displayInfo()
