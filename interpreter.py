# prompt user for mathematical expression
expression = input ('expression: ')

# assign the split to variables
x, y, z = expression.split()
x = float (x)
z = float (z)

# calculate and print
if y == '+':
    answer = x + z
elif y == '-':
    answer = x - z
elif y == '*':
    answer = x * z
elif y == '/':
    answer = x / z

print (answer)
