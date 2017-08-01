words = "it's thanksgiving day. It's my birthday, too!"
day = 'day'
print words.find(day)


print words.replace('day','month',2)

# minmax = [2,54,-2,7,12,98]

# def minmax(l,n):
#     maximum=l[0]
#     minimum=l[0]
#     for i in range(1,n+1):
#         if (l[i]>maximum):
#               max=l[i]
#         elif(n[i]<minimum):
#     return maximum
#     print minimum
#     print maximum

minmax = [2,54,-2,7,12,98]
print max(minmax)
print min(minmax)

x = ['hello',2,54,-2,7,12,98,'world']
arr = [x[0],x[-1]]
print arr


x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
y = x[:5]
del x[:5]
x.insert(0,y)
print x