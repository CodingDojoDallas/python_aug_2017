import random

def toss():
	#print toss summary
	attempt_count = 1
	head_count = 0
	tail_count = 0
	result = ""
	result_string = ""
#toss coin
	for i in range (0, 5000):
		new_toss = random.randint(0,1)
#toss result
		if new_toss == 1:
			head_count += 1
			result = "heads"
			print "Attempt #", attempt_count, ": Tossing a coin... It's a", result,"! Got", head_count, "heads so far and", tail_count, "tails so far."
		else:
			tail_count += 1
			result = "tails"
			print "Attempt #", attempt_count,": Tossing a coin... It's a", result,"! Got", head_count, "heads so far and", tail_count, "tails so far."
		attempt_count += 1

toss()
