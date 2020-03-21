
# defining a fucntion 
def print_twice(whatever):
    print(whatever)
    print(whatever)

#calling a fucntion 
#print_twice('Lily answered the questions')

#--------------------------------------------------------------
def double(a):
    return 2 * a
    print('The result is', 2 * a) # this line will never be reached

    

result = double(10)
print(f'The result of the function with argument 10 is {result}.')

#--------------------------------------------------------------------
# create function the returns absoulte value of any number 

def my_abs(number):
    """
    returns absoulte value of any number.

    number: an int.
    """
    #the above is called docstring
    if number < 0:
        return 0 - number
    else:
        return number
def main():
    #wrap test code in this function
    a = -10
    abs_a = my_abs(a)
    print(abs_a)

#print(my_abs(-10))

if __name__ == '__main__':
    #this will only be executed when running this file
    #it does not affect other files that import current module
    main()

#-----------------------------------------------------
#Final exercise in chapter 4 - Quadratic Function 
import cmath
#def Quadratic(a,b,c):
    
a = float(input('Enter a: ')) 
b = float(input('Enter b: '))  
c = float(input('Enter c: ')) 
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solutions are {0} and {1}'.format(sol1,sol2))






    
    

