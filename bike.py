
class Bike(object):
	def __init__(self,price,max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print 'Price is: $' + str(self.price)
		print 'Top speed: ' + str(self.max_speed) + 'mph'
		print 'Total miles: ' + str(self.miles)

	def drive(self):
		print 'Driving'
		self.miles += 10

	def reverse(self):
		print 'Reversing'
		if self.miles >= 5:
			self.miles -= 5
bike1 = Bike(100, 20)
bike1.drive()
bike1.drive()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(80, 15)
bike2.drive()
bike2.drive()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike(120, 9)
bike3.drive()
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
