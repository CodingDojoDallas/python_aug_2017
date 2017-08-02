#set lists to test

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

#define function

def compareLists(list_one, list_two):
	if list_one == list_two:
		print "These lists are the same"
	else:
		print "These lists are not the same"

print compareLists(list_one, list_two)
