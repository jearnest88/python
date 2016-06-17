
class Bike(object):
	def __init__(self,price,max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print 'Price is: $' + str(self.price)
		print 'Top speed: ' + str(self.max_speed) + 'mph'
		print 'Total miles: ' + str(self.miles)
		return self

	def drive(self):
		print 'Driving'
		self.miles += 10
		return self

	def reverse(self):
		print 'Reversing'
		if self.miles >= 5:
			self.miles -= 5
		return self
bike1 = Bike(100, 20)
bike1.drive().drive().reverse().reverse().displayInfo();

bike2 = Bike(80, 15)
bike2.drive().drive().reverse().reverse().displayInfo();

bike3 = Bike(120, 9)
bike3.drive().reverse().reverse().reverse().displayInfo();
