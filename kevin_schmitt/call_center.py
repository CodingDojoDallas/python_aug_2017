class Call(object):
    def __init__(self, call_id,name,number,time,reason):
        print 'I created a caller'
        self.id = call_id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def callinfo(self):
        print 'Here are the call attributes {}, {}, {}, {}, {}.'.format(self.id,self.name,self.number,self.time,self.reason)


class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)
    def add(self, call):
        #add the call to our list of calls
        self.calls.append(call)
        self.queue_size += 1
        return self
    def remove(self):
        self.calls.pop(0)
        self.queue_size -= 1
        return self
    # def info(self):
    #     for i in queue:
    #         print "{}: {}".format(self.name,self.number)
    #         print len(queue)

    # def search_remove(self, number):
    #     for i in range(0):
    #         if i == number:
    #            self.queue_list.pop(i) 

center = CallCenter()
dave = Call(231,'Dave','303-283-9485','8:43am','help')
center.add(dave)
# center.remove()
print center.calls
print center.queue_size