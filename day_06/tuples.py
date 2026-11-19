names_girls = ('Sara', 'Mizna', 'Iqra', 'Zoya', 'khyati',)
names_boys = ('muhammad', 'Moeen', 'Jamal', 'Amir', 'Talha')
names = names_boys + names_girls
print (names)
print (len (names))

girls = names[5:]
boys = names[:-5]
print (girls)
print (boys)
print ('Kausar' in girls)
del names