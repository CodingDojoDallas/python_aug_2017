# x=[4,6,1,3,5,7,25]

# def stars(arr):
#     for i in range(0,len(arr)):
#         print '*' * arr[i]
# stars(x)


x=[4,'tom',1,'michael',5,7,'jimmy smith']

def stars(arr):
    for i in arr:
        if isinstance(i,int):
            print '*' * i
        else:
            length = len(i)
            letter=i[0].lower()
            print letter * length
stars(x)