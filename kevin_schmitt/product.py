class product(object):
    def __init__(self, price, name, weight, brand, cost, status, tax):
        # print "i'm creating a product"
        self.price=price
        self.name=name
        self.weight=weight
        self.brand=brand
        self.cost=cost
        self.status=status
        self.tax=tax

    def checkprint(self):
        print "Here is my product info {},{},{},{},{},{},{}".format(self.price,self.name,self.weight,self.brand,self.cost,self.status,self.tax)
        return self

    def sold(self):
        self.status = 'sold'
        print "Here is my product info {},{},{},{},{},{},{}".format(self.price,self.name,self.weight,self.brand,self.cost,self.status,self.tax)
        return self

    def taxprice(self):
        self.price = self.price*(1+self.tax)
        print "My price after taxes will now be {}. THAT'S TOO MUCH!!!".format(self.price)
        return self

    def exchange(self):
        reason = raw_input('Please enter reason: exchange like new/exchange opened box/defective...')
        if reason == "exchange like new":
            print 'No problem. Let me help you with that!'
            print "Here is your updated product info ${}, {}, {}lbs, {}, ${} ,{}.".format(self.price,self.name,self.weight,self.brand,self.cost,self.status)
        if reason == "exchange opened box":
            self.status = 'used'
            self.price = self.price*0.8
            print 'No problem. Let me help you with that!'
            print "Here is your product's new info ${}, {}, {}lbs, {}, ${} ,{}.".format(self.price,self.name,self.weight,self.brand,self.cost,self.status)
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
            print "Oh no! Let's get rid of that one."
            print "Here is your updated product info ${}, {}, {}lbs, {}, ${} ,{}.".format(self.price,self.name,self.weight,self.brand,self.cost,self.status)
            return self





pro1 = product(25,'Clorox',8,'great value',12,'sold',.0825)
pro2 = product(14,'Cheerios',3,'general mills',2,'for sale',.0825)
pro3 = product(16,'Pizza',5,'digorno',10,'for sale',.0825)

# product.checkprint(pro2)
# product.sold(pro3)
# product.taxprice(pro1)
product.exchange(pro2)
# product.checkprint(pro1)
# product.checkprint(pro2)
# product.checkprint(pro3)