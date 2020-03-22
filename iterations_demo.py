print(1 +2 +3)

for i in range(5):
    print(i)


#for i in range(1000):
    #print(i+1)

#how to sum up all the intergers 

result = 0 

for i in range(10):
    print(f'In interation {i}, current result is {result}. ')

    result += i+1
    print(f'After adding {i+1}, the result becomes {result}.')
    print()

print(f'Final result is {result}.')    

for i in range(1,11,2):
    print(i)
    if i > 4:
        break

for i in range(0,11,2):
    print(i)
    if i == 4:
        continue
    print(i)

name = 'Smit'

for c in name:
    print(c)

for c in name:
    c = c.lower()
    print(c)

if name.startswith('S'):
    print('Yes')
else:
    print('No')

for c in name:
    print(c)
    if c == 'i':
        print('vowel is found!')
        

