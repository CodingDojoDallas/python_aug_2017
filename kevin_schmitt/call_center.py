class Call(object):
    def __init__(self, id,name,number,time,reason):
        print 'I created a caller'
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def callinfo(self):
        print 'Here are the call attributes{}, {}, {}, {}, {}.'.format(self.id,self.name,self.number,self.time,self.reason)



dave = Call(231,'Dave','303-283-9485','8:43am','help')

dave.callinfo()