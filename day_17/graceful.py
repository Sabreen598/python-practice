try:
    name = input ('Enter Your Name: ')
    year = int (input ('Enter your birth year: '))
    age = 2026 - year
    print (f'Your name is {name}, and you are {age}.') 
except ValueError: 
    print ('Value Error Occured.') 

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*Nordic_countries, es, ru = names
print(Nordic_countries, es, ru)