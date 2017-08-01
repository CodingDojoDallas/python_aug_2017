#odd/even
#count from 1-2000 and display odd/even

#define function
def odd_even():
	#go through range 1-2000 (exclusive last element)
	for count in range (1,2001):
		#if statement checks for odd number with modulo
		if count % 2 ==1:
			print "Number is {}. This is an odd number.".format(count)
		#else even
		else:
			print "Number is {}. This is an even number.".format(count)
#figure out why there is still a none returned
odd_even()
