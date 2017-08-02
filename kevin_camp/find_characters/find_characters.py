#input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
#variables
new_list = []
count = 0
#for loop
for item in word_list:
	if item.find(char) != -1:
		new_list.append(item)
#print list
print new_list
