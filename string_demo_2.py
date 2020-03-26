# built-in functions that take string(s) as parameters

#print('John')
#input('Please enter your name:   ')
#type('John')
#len('John')
#int('1') / float('1.23') / bool('John')

team='New England Patriots'
letter = team[1]
print(letter)

print(team[0])

#print(team[1.5])
#print(team[1.0])

print(len(team))

last = team[len(team)-1]
# a better way
last = team[-1]
print(last)

for letter in team:
    print(letter)

prefixes ='JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print(letter+suffix)

#Exercise 1
for letter in prefixes:
    if letter =='O' or letter == 'Q':
        print(letter + 'u' + suffix)
    else:
        print(letter+suffix)

# string slicing
team='New England Patriots'

print(team[0:11]) #can remove 0 
print(team[12:20]) #can remove 20

print(team[:])

print(team[::2])

print(team[::-1])

#team[12:20]= 'Seahawks' --> cannot do this

new_team = team[:12] +'Seahawks'
print(new_team)
print(team)


#searching
def find(word, letter):
    index = 0 
    while index < len(word):
        if word[index]==letter:
            return index 
        index = index + 1 
    return -1 
print(find(team,'E'))


#counting
team ='New England Patriots'
count = 0 

for letter in team:
    if letter == 'a':
        count += 1
print(count)

#string methods

new_team= team.upper()
print(new_team)

another_team = team.lower()
print(another_team)

print(team.split())

s = '       abcd      '
print(s.strip())

#exercise 5

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

            #THE ABOVE FUNCTION IS FLAWED BECAUSE IT WILL ONLY LOOK AT THE FIRST LETTER OF THE STIRNG. THIS IS BAD BECAUSE IT MAY END EARLY ONCE IT RESULTSIN FALSE, FOR EXAMPLE "Smit" WOULD RETURN FALSE SINCE THE 1ST LETTER 'S' IS UPPERCASE
        
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

            #THE ABOVE FUNCTION IS FLAWED BECAUSE LINE 106, c IS PLACED IN '' MAKING IT A STRING AND CONFUSING PYTHON

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

            #THE ABOVE FUNCTION IS FLAWED BECAUSE FOR EXAMPLE 'smiT', IT WOULD RETURN TRUE FOR 's','m','i', BUT THE UPPERCASE LAST LETTER, 'T', WOULD BE FALSE


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

            #THE ABOVE FUNCTION IS FLAWED BECAUSE FLAG IS SET TO FALSE BY DEFAULT AND WILL REMIAN THAT WAY UNTIL  IT ENOCUNTERS A LOWERCASE IN WHICH IT CAN NOT BE REVERTED BACK TO FALSE 
            

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

            #THE ABOVE FUNCTION IS FLAWED BECAUSE IT CHECKS TO SEE IF THE WHOLE STRING IS LOWER CASE OR NOT 

#exercise 6 

#refer to "Python_challenge.py" file in the same repositroy as this file. 
