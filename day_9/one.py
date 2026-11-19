age = int (input ('what is your age?: '))
if age >= 18:
    print ('You are old enough to drive.')
elif age <= 18:
    print (f'You need {18 - age} more years to learn to drive.')    