my_pot = ['beans', 'potatoe', 'plantain', 'ugwu', 'porridge']
char= "0"

def find_char(arr, str):
    my_pot =[]
    for word in arr:
        if str in word:
            my_pot.append(word)
    return my_pot


print find_char(my_pot,char)        
