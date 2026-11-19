# square of # of side 8
for row in range (0, 8):
    for col in range (0, 8):
        print ('# ', end = '')
    print ()

for i in range (0, 11):
    print (f'{i} x {i} = {i ** 2}')

# all odd number.....even if start the range with 0
for a in range (1, 101, 2):
    print (a, ' ', end = '')


sum = 0
for h in range (0, 101):
    sum = sum + h
print (sum)    

from countries import countries
for i in countries:
    if i.endswith('land'):
        print (i)

fruits = ['banana', 'orange', 'mango', 'lemon'] 
for k in reversed(fruits):
    print (k)

from countries_data import con

# all the languages
lans = 0
for r in con:
    lans = lans + len (r['languages'])
print (lans)

language_count = {}
for entry in con:
    for lang in entry['languages']:
        if lang in language_count:
            language_count[lang] += 1
        else:
            language_count[lang] = 1

sorted_languages = sorted(
    language_count.items(), 
    key=lambda x: x[1], 
    reverse=True
)

top_count = 0
for lang, freq in sorted_languages:
    if top_count >= 10:
        break  
    top_count += 1
    print(f"{lang}: {freq} times")
