import functools

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

contupp = map (lambda x: x.upper(), countries)
print (list (contupp))

numsqu = map (lambda x: x ** 2, numbers)
print (list (numsqu))

def landing(n):
    if n.startswith ('E') or n.endswith ('land'):
        return True
    return False

land = filter (landing, countries)
print (list (land))

def lettercount (country):
    if len (country) == 6:
        return True
    return False

letter = filter (lettercount, countries)
print (list (letter))

