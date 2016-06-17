class mathDojo(object):
    def __init__(self):
        print ('I am math')
        self.sum = 0
    def add(self, *number):
        for arg in number:
            if(isinstance(arg, list) or isinstance(arg, tuple)):
                for val in arg:
                    self.sum = self.sum + arg
            else:
                self.sum = self.sum + arg
        return self
    def subtract(self, *number):
        for arg in number:
            if(isinstance(arg, list) or isinstance(arg, tuple)):
                for val in arg:
                    self.sum = self.sum - val
            else:
                self.sum = self.sum - arg
        return self

math = mathDojo()
math.add(2,2,3,4).add(56,9).subtract(3,6,8)

print(math.sum)
