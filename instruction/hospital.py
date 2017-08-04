import random

class Patient(object):
    def __init__(self, name, allergies):
        self.id = random.randint(1, 10000)
        self.name = name
        self.allergies = allergies
        self.bed_number = None


class Hospital(object):
    def __init__(self, name):
        self.patients = []
        self.name = name
        self.capacity = random.randint(10, 30)
    
    def admit(self, patient):
        if len(self.patients) == self.capacity:
            print 'We are at full capacity'
            return self
        else:
            self.patients.append(patient)
            patient.bed_number = len(self.patients) - 1


class Something(Hospital):
    def __init__(self):
        super(Something, self).__init__('something')
        # pass

class Works(Something):
    def __init__(self):
        super(Works, self).__init__()
        # pass


x = Works()
print  x.capacity
# a = Patient('Bob', [])
# b = Patient('Cody', [])

# c = Hospital('Codys Hospital')

# c.admit(a)
# c.admit(b)
# print a.bed_number
# print b.bed_number
