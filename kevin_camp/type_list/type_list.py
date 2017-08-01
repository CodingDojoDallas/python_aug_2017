#input
mixed_list = ['magical unicorns', 19, 'hello', 98.98, 'world']
integer_list = [1,2,3,4,5]
string_list = ["Okey", "Dokey", "Daddy"]

#define function for type
def id_list_type(my_list):
	my_string = ""
	total = 0
#for loop through list items
	for value in (my_list):
		if isinstance(value, int) or isinstance(value, float):
			total += value
		elif isinstance(value, str):
			my_string += value
#if loop for mixed type
	if my_string and total:
		print "The array you entered is of mixed type"
		print "String:", my_string
		print "Total:", total
#elif loop for string type
	elif my_string:
		print "The array you entered is of string type"
		print "String:", my_string
#else loop for number type
	else:
		print "The list that you entered is of number(float or int) type"
		print "Total:", total
#run function
print id_list_type(mixed_list)
print id_list_type(integer_list)
print id_list_type(string_list)
