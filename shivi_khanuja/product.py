class Product(object):
    def __init__(self, item_name, weight, price, brand, status):
        self.item_name = item_name
        self.weight = weight
        self.price = price
        self.brand = brand
        self.status = status            
    

    def displayInfo(self):
        print 'Item name is: ' + str(self.item_name)
        print 'Weight is ' + str(self.weight) 
        print 'Item is by ' + str(self.brand) + ' brand'
        return self

    def totalprice(self):
        tax = 0.0825
        self.price += tax
        print self.price

    def return1(self):
        if self.status == 'defective':
            self.price = 0
            print 'Price is $ ' + str(self.price)
        elif self.status == 'used':
            print "Price is $" .format(self.price * 0.20)    
        else:
            print "For Sale " + "Price is $" + str(self.price)

        return self

    
             

product1=Product('tidepods', 200, 4.60, 'tide', 'used' )
product2=Product('Box', 50, 5.60, 'rubbermaid', 'new' )
product3=Product('shorts', 100, 24.99, 'Merona', 'defective' )
product1.displayInfo().return1().totalprice()
print "  "
product3.displayInfo().return1().totalprice()
print "  "
product2.displayInfo().return1().totalprice()
print "  "
