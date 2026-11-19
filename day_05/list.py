empty_list = []
hobbies = ['reading', 'puzzling', 'writing', 'baking', 'learning', 'praying']
print (len (hobbies))
print (hobbies [0])
print (hobbies [-1])
print (hobbies [round (len (hobbies)/ 2)])
mixed_data_types = ['sabreen', 18, 1.55, 'umarried', ''' 1 Nehru Nagar, Raiya Road, Rajkot ''']
it_companies = ['Apple', 'Microsoft', 'IBM', 'Facebook', 'Google', 'Oracle', 'Amazon']
it_companies[3] = 'Flipkart'
print (it_companies)
it_companies.append('Facebook')
it_companies[5].upper()
print(it_companies)
print ('IBM' in it_companies)
it_companies.sort()
print (it_companies)
it_companies.sort(reverse = True)
print (it_companies)
print (it_companies[0:3])
print (it_companies[4:])
it_companies.pop(0)
print (it_companies)
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print (front_end + back_end)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
range = max_age - min_age
first, second, third, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print (first)
print (second)
print (third)
print (scandic)




