import random
def coin_toss(flips):
    heads = 0
    tails = 0
    flip_num = 1

    for x in range(1,flips):
        new_toss = random.randint(0,1)
        if new_toss == 1:
            heads+=1
            result = 'heads'
            print "Attempt #", flip_num, ": Throwing a coin... It's a", result, "! Got ", heads, "head(s) so far and", tails, "tail(s) so far"
        else:
            tails += 1
            result = 'tails'
            print "Attempt #", flip_num, ": Throwing a coin...It's a", result, "! Got", heads, "head(s) so far and", tails, "tail(s) so far."
        flip_num += 1
# t=5001
t=51
coin_toss(t)

   # attempt_count = 1
    # head_count = 0
    # tail_count = 0
    # result = ""
    # result_string_complete = "Attempt #", flip_num, ": Throwing a coin... It's a ", result, "! Got ", heads, "head(s) so far and", tails, "tail(s) so far"

    # for x in range(1, reps):
        # new_toss = random.randint(0,1)
        # if new_toss == 1:
            # head_count += 1
#             result = "head"
#             print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
#         else:
#             tail_count += 1
#             result = "tail"
#             print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
#         attempt_count += 1

# toss(5001)
