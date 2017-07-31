print 'Hello World!'

x = 'Hello Python'
print x
y = 42
print y

name = 'Zen'
print 'My name is',name

name = 'Zen'
print 'My name is' + name

first_name = 'Zen'
last_name = 'Coder'
print 'My name is {} {}'.format(first_name, last_name)

hw = 'hello %s' % 'world'
print hw
x = "Hello World"
print x.upper()
# output:
"HELLO WORLD"

fruits = ['apple','banana','orange','strawberry']
vegetables = ['lettuce','cucumber','carrots']

fruits_and_vegetables = fruits + vegetables
print fruits_and_vegetables
salad = 3 * vegetables
print salad

drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print drawer[0]  #prints documents
#access the drawer with index of 1 and print value
print drawer[1] #prints envelopes
#access the drawer with index of 2 and print value
print drawer[2] #prints pens

x = [1,2,3,4,5]
x.append(99)
print x
#the output would be [1,2,3,4,5,99]

x = [99,4,2,5,-3];
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];

my_list = [1, 'Zen', 'hi']
print len(my_list)
# output
#3

my_list = [1,5,2,8,4]
my_list.append(7)
print my_list
# output:
# [1,5,2,8,4,7]

age = 15
if age >= 18:
  print 'Legal age'
else:
  print 'You are so young!'

  if age >= 18:
  print 'Legal age'
elif age == 17:
  print 'You are seventeen.'
else:
  print 'You are so young!'
  