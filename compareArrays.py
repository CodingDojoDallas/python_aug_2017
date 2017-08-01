list1 = [1,2,5,6,2]
list2 = [1,2,5,7,11]

elems_in_both_lists = set(list1) & set(list2)
print elems_in_both_lists
if list1 == elems_in_both_lists:
    print 'These are the same list'
else:
    print "THESE AIN'T THE SAME"