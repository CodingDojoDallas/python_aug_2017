class Call(object):
    def __init__(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    def display(self):
        print 'Caller information:unique_id-{},caller_name-{}, phone_number-{}, time_of_call-{}, reason_for_call-{}.'.format(self.unique_id,self.caller_name,self.caller_phone_number,self.time_of_call,self.reason_for_call)

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)
    #add a new call to the end of the call list
    def add(self, call):
        self.calls.append(call)
        return self
    def remove(self, call):
        self.calls.pop(0)
        return self
    def info(self):
        for call in queue:
            print"{}, {}".format(self.name,self.number)
            print len(queue)

        
place = CallCenter()
kyle = Call(312654, 'kyle', 654-654-6547, '3:00pm', 'questions')

print place.info()