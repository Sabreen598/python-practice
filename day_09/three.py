fru = input ('Name a fruit: ')
fruits = ['banana', 'orange', 'mango', 'lemon']

if fru in fruits:
    print ('This fruit already exists in the list.')
else: 
    fruits.append(fru)
    print (fruits)    