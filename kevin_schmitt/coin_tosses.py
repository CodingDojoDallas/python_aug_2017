# import random

# def coinToss():
#     number = input("Number of times to flip coin: ")
#     recordList = []
#     heads = 0
#     tails = 0
#     flip = random.randint(0, 1)
#     if (flip == 0):
#         print("Heads")
#         recordList.append("Heads")
#     else:
#         print("Tails")
#         recordList.append("Tails")
#     print(str(recordList))
#     print(str(recordList.count("Heads")) + str(recordList.count("Tails")))
# coinToss()


import random
def coinToss():
    number = input("Number of times to flip coin: ")
    recordList = []
    heads = 0
    tails = 0
    round = 0
    for amount in range(number):
         flip = random.randint(0, 1)
         
         if (flip == 0):
              print("It's a Heads",)
              recordList.append("Heads")
         else:
              print("It's a Tails")
              recordList.append("Tails")
    print(str(recordList))
    print(str(recordList.count("Heads")) , str(recordList.count("Tails")))
coinToss()