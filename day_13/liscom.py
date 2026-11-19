numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
sort = [i for i in numbers if i < 1]
print (sort)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [i for row in list_of_lists for i in row]
print (flat)

# expression for i in range....
#here this will generate a list the expression is to be the every individual tuple that needs to be generated
finallist = [(i, 1) + tuple (i ** j for j in range (1, 6)) for i in range (11)]
print (finallist)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country = [
    [country.upper(), country[:3].upper(), capital.upper()]
    for inner_list in countries
    for country, capital in inner_list
]
print (country)
#output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

result = [
    {'country': country, 'city': city}
    for inner_list in countries
    for country, city in inner_list
]

print(result)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']