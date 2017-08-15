class math(object):
    def __init__(self):
        self.result=0
    def add(self, *nums):
        for num in nums:
            if type(num) == list or type(num) == tuple:
                for k in num:
                    self.result += k
            else:
                self.result += num
        return self
    def subtract(self, *nums):
        for num in nums:
            if type(num) == list or type(num) == tuple:
                for k in num:
                    self.result -= k
            else:
                self.result -= num
        return self
        print math().add([1],3,7).add([5, 8, 7, 2], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result