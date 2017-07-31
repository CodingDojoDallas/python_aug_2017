#find and replace
words = "It's thanksgiving day. It's my birthday, too!"
words.find("day")
words = words[:18] + "month" + words[21:]
print words

#min and max
x = [2,54,-2,7,12,98]
print max(x)
print min(x)

#first and last
x = ["hello",2,54,-2,7,12,,98,"world"]
newlist = x[0],x[-1]
print newlist

#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
firstlist = x[:5]
secondlist = x[5:]
newlist = [firstlist], secondlist
print newlist