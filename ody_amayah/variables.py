class user(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False

    def login(self):
        self.logged = True
        print self.name + 'is logged in.'
        return self

new_user = user('ody','emmayah2@ody.com')
print new_user.email