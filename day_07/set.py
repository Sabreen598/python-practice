# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print (len (it_companies))
it_companies.add ('twitter')
it_companies.update([ 'Oracle', 'Amazon'])
print (it_companies)
it_companies.remove ('twitter')
it_companies.discard ('Oracle')
print (it_companies)

C = A.union(B)
print (C)
D = A.intersection(B)
print (D)
print (A.subset(B))
print (B.subset(A))
print (A.disjoint(B))
print (A.symmetric_difference(B))
print (A.difference(B))
del A
del B

age_set = set (age)
