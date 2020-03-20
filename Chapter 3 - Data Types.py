import math
print(math.pi)
print(math.sqrt(85))
#----------------------------------------------------------------------------------------
import random
print(random.random())
print(random.choice([1,2,3,4]))
#print(random.seed(42))
print(random.randint)
print(random.choice('Smit'))
print(random.choice(['Superman','Spiderman','Wonder Woman','Captain Marvel']))
print(random.randint(1,6))
#---------------------------------------------------------------------------------------------
for i in range(10):
    print(i)

for i in range(10):
    print(random.randint(1,6))

#----------------------------------------------------------------------------------
print('I\'m learning\nPython.')

3>2
3>5

#age = input('Please enter your age: ')
#if age >= 21:
#    print('Yes, you can.')
#else:
#    print('Sorry, nice try bud haha!')
#---------------------------------------------------------------------------------------------
print(2**100)
print(str(2**100))
print(len(str(2**100)))
#print(2**1000000)
#print(len(str(2**1000000)))
#----------------------------------------------------------------------------------------------
import math
print(math.pi)
print(math.sqrt(4))
#-----------------------------------------------------------------------------------
#Calling a fucntion from another file (files must be in same folder)

#import myabs
from 'Chapter 4 - Funtions' import my_abs

b = -42
abs_b = 'Chapter 4 - Functions'.my_abs(b)
print(abs_b)


