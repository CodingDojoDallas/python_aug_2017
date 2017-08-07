class Call():
    def __init__(self, id1, name, phone_number, time, reason):
        self.id1 = id1
        self.name = name
        self.phone = phone_number
        self.time = time
        self.reason = reason

    def display(self):
        print "ID:" + self.id1
        print "Name:" + self.name
        print "Phone:" + self.phone
        print "Time of Call" + self.time
        print "Reason for call:" + self.reason
        print len(self.call)
# Call("01", "Sean", "55555555555", "7:00 AM", "Flat Tire").display()

class CallCenter(?):
    def __init__(self, call):
        self.call
        self.queue = len(self.call)
#        print len(self.call)

    def call(self):
        self.queue.append(?)
        return self

    def remove(self):
        self.call.remove(self.call[0])
        return self

    def info(self):
        print str(self.queue) + "calls in queue."
        return self

Call("01", "Sean", "55555555555", "7:00 AM", "Flat Tire").display()

# CallCenter([1,2,3]).remove().info()
