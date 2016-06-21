class Underscore(object):
    def map(self, arr, callback):
        arrnew = []
        for data in arr:  #cycles through the numbers in the original array
            arrnew.append(callback(data))  #performs the lambda method on number and adds it to the new array
        return arrnew

    def reduce(self, arr, callback, start = None):
        it = iter(arr)
        if start is None:
            try:
                start = next(it)
            except StopIteration:
                raise TypeError('no initial value')
        newValue = start
        for data in arr:
            newValue = callback(newValue, data)
        return newValue

    def find(self, arr, callback):#adds qualifying numbers to the new array
        arrnew = []
        for data in arr: #cycles through array
            if callback(data) == True: #checks if number meets lamdba
                arrnew.append(data) #adds qualifying numbers to the new array
        return arrnew

    def filter(self, arr, callback):
        arrnew = []
        for data in arr:  #same as find
            if callback(data) == True:
                arrnew.append(data)
        return arrnew

    def reject(self, arr, callback): #this is just the opposite of filter
        arrnew = []
        for data in arr:
            if callback(data) == False:
                arrnew.append(data)
        return arrnew


_ = Underscore()
nums = [1,2,3,4,5,6]

mapMeth = _.map(nums, lambda x: x * 2)
print mapMeth

reduceMeth = _.reduce(nums, (lambda x,y: x*y))
print reduceMeth

findMeth = _.find(nums, lambda x: x % 2 == 0)
print findMeth

filterMeth = _.filter(nums, lambda x: x % 2 == 0)
print filterMeth

rejectMeth = _.reject(nums, lambda x: x % 2 == 0)
print rejectMeth
