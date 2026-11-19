import re

txt = 'I love to teach python and Javascript'
matches = re.match ('I love', txt, re.I)
print (matches.span())

paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''

blah = r'[A-Za-z]+'
reg = re.findall(blah, paragraph)
count = {}
for reg in reg:
    if reg in count:
        count[reg] = count[reg] + 1
    else:
        count[reg] = 1

print (count.items())