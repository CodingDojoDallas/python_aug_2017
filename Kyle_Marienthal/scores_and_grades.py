# write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

import random
for x in range(10):
    x=random.randint(60,100)
    if x > 60 and x < 69:
        print "Score:", x, "; Grade - D"
    elif x > 70 and x < 79:
        print "Score:", x, "; Grade - C"
    elif x > 80 and x < 89:
        print "Score:", x, "; Grade - B"
    else:
        print "Score:", x, "; Grade - A"
    