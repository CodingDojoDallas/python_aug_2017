#generate 10 random scores between 60 & 100
import random

def grade(iters):
	print "Scores and Grades"
#for loop with if elifs
	for i in range(0, iters):
		score = random.randint(60, 101)

		if score <=69:
			print "Score:", score,";Your grade is D"
		elif score >=70 and score <=79:
			print "Score:", score,";Your grade is C"
		elif score >=80 and score <=89:
			print "Score:", score,";Your grade is B"
		else:
			print "Score:", score,";Your grade is A"
	print "End of program. Bye!"

grade(10)
