# takes a list and print a message for each index based on its type

# use type() for the ifs *****
#  if str, concatenate it to a new str *****
#  if int, sum += that int*****
# print string, #, and the type
# if more than one type print = mixed
px = ['magical unicorns',19,'hello',98.98,'world']
def typeList(x):
    total = 0
    myString = ''
    for value in x:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            myString += value
    if total:
        print "this is an integer list"
        print "Sum: " , total
    elif myString:
        print "this is a list of strings"
        print "String: " + myString
    else:
        print "the list is a mixed type"
        print "Sum: " , total
        print "String: " + myString

typeList(px)

                
    # if type(i) == str:
    #     print i + " is what your string says."

