# for check in range(0,4,1):
#     print '* * * *'
#     print ' * * * *'


def multiply(arr,num):
    print arr, num
    for x in arr:
        print x
        x *= num
    return arr

a = [2,4,10,16]
b = multiply(a,5)
print b