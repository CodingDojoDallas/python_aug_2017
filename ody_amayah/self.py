class User(object):
  name = "Anna"
  anna = User()
  print "anna's name: ", anna.name
  User.name = "Bob"
  print "anna's name after change:", anna.name
  bob = User()
  print "bob's name:", bob.name