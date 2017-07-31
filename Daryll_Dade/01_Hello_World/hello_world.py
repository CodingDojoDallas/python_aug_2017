print "Hello World"
x = "Hello Python"
print x
y = 42
print y
# commenting a single line
# we can even comment out code
# print "this will not print!"
print "read below for more on multi-line comments in python!" #this would execute
# This line and below would not execute
'''
Triple quotations allow us to comment across multiple lines as long as
the triple quoted comment is not the first thing in your file.
You can use double or single quotes!
'''
print "this is a sample string"
name = "Zen"
print "My name is", name

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

hw = "hello %s" % 'world'
print hw
# the output would be:
# hello world

x = "Hello World"
print x.upper()
# output:
"HELLO WORLD"

ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []
