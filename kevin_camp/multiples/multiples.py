#multiples part 1
for x in range(1,100):
    if x % 2 == 1:
        print x

#multiples part 2
for x in range(5,1000001):
    if x % 5 == 0:
        print x

#sum list
a = [1,2,5,10,255,3]
sum = 0
for i in a:
	sum += i
print sum

#average list
a = [1,2,5,10,255,3]
sum = 0
for i in a:
	sum += i
avg = sum/len(a)
print avg
