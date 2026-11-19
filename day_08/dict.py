dog = {'name': 'Bob', 'Breed': 'Husky', 'legs': 4, 'age': 12}
student = {
    'first_name' : 'Sabreen',
    'last_name' : 'Dangasiya',
    'gender' : 'female',
    'age' : 18,
    'skills' : ['python', 'C'],
    'country' : 'India'
}
print (student)
print (len (student))
print (type (student ['skills']))
student ['skills'].append('javascript')
print (student ['skills'])
print (student.keys())
print (student.values())
print (student.items())
del student ['country']
student.pop ('gender')
print (student)
del dog