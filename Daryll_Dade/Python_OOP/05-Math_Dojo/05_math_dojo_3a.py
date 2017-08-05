import math

class MathDojo(object):
    def __init__(self, *nums):
        self.result = 0

    def add(self, *nums):
        for num in nums:
            if type(num) == list or type (num)== tuple:
                for number in num:
                    self.result += self.number
                else:
                    self.result += self.number
            print "{} is the total of your input".format(self.result)
        return self

    def subtract(self, *nums):
        for num in nums:
            if type(num) == list or type(num) == tuple:
                for number in num:
                    self.result -= number
                else:
                    self.result -= number
        return self


x =  MathDojo(25, 20)
y = 20
print x.add()

# print y.add()
