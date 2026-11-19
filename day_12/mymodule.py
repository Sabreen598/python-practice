import random
import string
def user_id_gen_by_user():
    a = int (input ('number of characters: '))
    b = int (input ('number of ids to generate: '))
    key = string.ascii_letters + string.digits
    
    for i in range (b):
        id = ''.join (random.choices (key, k = a))
        print (id)
    return id
