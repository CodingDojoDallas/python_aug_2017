sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

i = bI
if i >= 100:
    print "thats a big number"
elif i < 100:
    print 'thats a small number'
else:
    print 'number aint got no value'


string = bS
if len(string)>=50:
    print 'long sentence'
elif len(string)<50:
    print 'short sentence'

list = lL
if len(list)>=10:
    print 'big list!'
elif len(list)<10:
    print 'short list!'

mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [2,3,1,7,4,12]
string_list = ['magical','unicorns']

def type_list(lst):
    new_string = ''
    total = 0

    for value in lst:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            new_string += value

    if new_string and total:
        print "The array you entered is of mixed type"
        print "String:", new_string
        print "Sum:", total

    elif total:
        print "The array you entered is of integer type"
        print "Sum:", total

    else:
        print "The array you entered is of string type"
        print "String:",new_string

print type_list(mixed_list)
print type_list(integer_list)
print type_list(string_list)