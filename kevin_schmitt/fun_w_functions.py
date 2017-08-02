
for i in range(1,1001):
    num = i
    if (i % 2 == 1):
        print "Number is " + str(num) + '.' + " This an odd number!"
    else:
        print 'Number is ' + str(num) + '.' + 'This is an even number!!'

x = [1,2,3,5,8]
def multiply(arr):
    for i in range(0,len(arr)):
        arr[i] = arr[i]*5
    return arr
print multiply(x)


# def layered_multiples(arr):
#     print arr
#     new_arr = []
#     for i in arr:
#         var_arr = []
#         for x in range(0,i):
#             var_arr.append(1)
#         new_arr.append(var_arr)
#     return new_arr
# get = layered_multiples(multiply(x*3))

def layered_multiples(arr):
    print arr
    new_arr = []
    for i in arr:
        var_arr = []
        for x in range(0,i):
            var_arr.append(1)
        new_arr.append(var_arr)
    return new_arr

x = layered_multiples(multiply([2,4,5]*3))
print x