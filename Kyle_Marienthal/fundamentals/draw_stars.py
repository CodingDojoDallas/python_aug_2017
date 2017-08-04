# def drawStars(arr):
#     for idx in arr:
#         print '*'* idx

# x = [4,6,1,3,5,7,25]
# drawStars(x)



def drawStars(arr):
    for idx in arr:
        if isinstance(idx, int):
            print '*'* idx
        else:
            word = idx.lower()
            print word[0] * len(word)

        




x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
drawStars(x)