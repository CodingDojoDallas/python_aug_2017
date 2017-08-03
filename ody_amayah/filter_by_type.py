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


#integer
variable = mL
if variable >= 99:
    print "that's a big fucking number"
else:
    print 'thats a small number'   


#strings
variable = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
if len(variable) >= 100:
    print 'long sentence'
else:
    print 'short sentence'    

#Lists
variable = mL
if isinstance(variable, list):
    if len(variable) >= 10:
        print 'big list'
    else:
        print 'short list'    


        # set one of the above variables as the current one I'm testing
current_tester = lL

curr_type = type(current_tester)
if curr_type is int:
    if current_tester >= 100:
        print "That's a big number!"
    else:
        print "That's a small number!"
elif curr_type is str:
    if len(current_tester) >= 50:
        print "Long sentence."
    else:
        print "Short sentence."
elif isinstance(current_tester, list):
    if len(current_tester) >= 10:
        print "Big list!"
    else: 
        print "Short list."            