#find and replace
words = "it's thanksgiving day. it's my birthday,too!"
print words.find('day')
print words.replace('day', 'month') 

#min and max
x = [2,54,-2,7,12,98]
print 'min:', min(x) #print min(x)
print 'max:', max(x) #print max(x)

#first and last
x = ["hello",2,54,-2,7,12,98,"world"]
print(x[0]+x[7])  #print x[0], x[len(x)-1]

#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
single_digits = [-3, -2, 2, 6, 7]
double_digits = [10, 12, 19, 32, 19, 54, 98]
single_digits_double_digits= single_digits + double_digits
print single_digits_double_digits


print x
x.sort()
print x
first_list = x[:len(x)/2] # optional first parameter of slice defaults to zero
second_list = x[len(x)/2:] # optional second parameter of slice defaults to the list's length
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list