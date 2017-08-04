# *************odd/even**************
# def oddEven():
#     for i in range(1,2001):
#         if i % 2 == 0:
#             print 'Number is ', i,'. This is and even number'
#         else:
#             print 'Number is ', i,'. This is an odd number'

# oddEven()

#************multiply****************
myArr = []
def multiply(arr,num):
    for i in arr:
         myArr.append(i * num)
    return myArr

arr = [2,4,10,16]
b = multiply(arr, 5)
# print b
#********hacker challenge************
def layered_multiples(arr):
    new_array = []
    for x in arr:
        ones_arr = []
        for val in range(0,x):
            ones_arr.append(1)
        new_array.append(ones_arr)
    return new_array

x = layered_multiples([6, 12, 15])
print x