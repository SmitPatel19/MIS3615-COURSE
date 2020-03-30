a = []
print(type(a))

print(len(a))

a = [10,20,30,40]

print(len(a))

b = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
print(len(b))
print(type(b))
print(type(b[0]))
print(len(b[0]))

c = ['spam', 2.0, 5, [10, 20]]
print(type(c))
print(type(c[0]))
print(type(c[-1]))

#list are mutable 
AFC_East = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
AFC_East[3]= 'New York Giants'

print(AFC_East[3])