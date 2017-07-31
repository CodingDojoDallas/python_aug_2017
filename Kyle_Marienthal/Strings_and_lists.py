#find and replace
words = "It's thanksgiving day. It's my birthday, too"
# string.find(substring): returns the index of the start of the first occurrence of substring within string.
print words.find('day')
print words.replace('day','month')

# min and max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

# first and last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[-1]
y = [x[0],x[-1]]
print y

# new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
first_part = x[:len(x)/2]
second_part = x[len(x)/2:]
second_part.insert(0,first_part)
print second_part