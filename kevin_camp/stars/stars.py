print "Part 1"
# given array of ints, print rows of stars
def draw_stars(arr):
	for i in arr:
		print "*" * i

user_arr = [4,6,1,3,5,7,25]
draw_stars(user_arr)

print "Part 2"

def stars_chars(arr):
	for i in arr:
		if isinstance(i,int):
			print "*" * i
		elif isinstance(i,str):
			letter = i[0].lower()
			print letter * len(i)
		else:
			return "error"

user_arr2 = [4,'Tom',1,'Michael',5,7,'Jimmy Smith' ]
stars_chars(user_arr2)
