class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    
#  Sell: changes status to "sold"
    def sell(self):
        self.status = "sold"
        print self.status
        return self

#  Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
    def add_tax(self,tax):
        self.price += tax
        return self.price

#  Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective change status to defective and change price to 0. If it is being returned in the box, like new mark it as for sale. If the box has been opened set status to used and apply a 20% discount.
    def giveBack(self, reason):
        if reason == "defective":
            print 'test 1'
        elif reason == "like new":
            print 'test 2'
        elif reason == "opened":
            print 'test 3'
            # self.status = "used"
            # self.price += price* 1/5

product1 = Product(.10,"apple", .5, "Fuji", .40)
tax = .08
product1.giveBack('opened')


# Product Class:
# Attributes:
#  Price
#  Item Name
#  Weight
#  Brand
#  Cost
#  Status: default "for sale"
# Methods:
#  Sell: changes status to "sold"
#  Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
#  Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective change status to defective and change price to 0. If it is being returned in the box, like new mark it as for sale. If the box has been opened set status to used and apply a 20% discount.
#  Display Info: show all product details.