import math

class MathDojo(object):
    def __init__(self,*nums):
        self.result = 0


    def add(self, arg1, *nums):
        # for num in nums:
        #     if type(num) == list or type (num)== tuple:
        #         for number in num:
        #             self.result = num
        #         else:
        #             self.result = num
        #     print "{} is the total of your input".format(self.result)
        print ""{},{}""
        return self.result

    def subtract(self,arg1, *nums):
        for num in nums:
            if type(num) == list or type(num) == tuple:
                for number in num:
                    self.result -= number
                else:
                    self.result -= number
        return self.result


x =  MathDojo(25, 20)
print(x.add(1,2))
y = MathDojo(100,[1,2,3,4,5])

x.add(10,5)

print x
print y

# print y.add()
