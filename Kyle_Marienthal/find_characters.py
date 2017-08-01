def find_char(arr, str):
    # print arr
    # print str
    myList= []
    for word in arr:
        if str in word:
            myList.append(word)
    return myList

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
print find_char(word_list, char)
