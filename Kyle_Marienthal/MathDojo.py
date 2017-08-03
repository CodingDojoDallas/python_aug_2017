class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *nums):
        for num in nums:
            self.result += num
        return self

    def subtract(self, *nums):
        for num in nums:
            self.result -= num
        return self

md = MathDojo()
print md.add(2).add(2, 5).subtract(3, 2).result