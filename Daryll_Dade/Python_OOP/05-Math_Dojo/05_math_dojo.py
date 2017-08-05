class MathDojo(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        total1= num1+num2
        print total1
        return self

    def subtract(self):
        total2 = num1-num2
        print total2
        return self

    def display_nums(self):
        print "{}  {} health.".format(self.num1, self.num2)
        return self

ten_fifteen = MathDojo(10, 15)

ten_fifteen.add().display nums

    
