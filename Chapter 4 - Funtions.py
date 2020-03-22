
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

#a = float(input('Enter a: ')) 
#b = float(input('Enter b: '))  
#c = float(input('Enter c: ')) 
#d = (b**2) - (4*a*c)
#sol1 = (-b-cmath.sqrt(d))/(2*a)  
#sol2 = (-b+cmath.sqrt(d))/(2*a)
#print('The solutions are {0} and {1}'.format(sol1,sol2))


import math
def quadratic(a,b,c):
    """
    return the two solutions of a quadratic function, a*x**2+b*x+c=0, if there are real number solutions
    a,b,c:float values
    """
    discriminant = b**2 - 4 * a *c
    if discriminant >= 0:
         x_1 = (-b + math.sqrt(discriminant))/ (2 * a)
         x_2 = (-b - math.sqrt(discriminant))/ (2 * a) 
         return x_1, x_2
    else:
        #print ('No real number solutions.')
        return None, None

    return x_1, x_2
    #print('The results are', x_1, x_2)

#TODO: what to return when there is no real number solution
#TODO: wrap test code into main function 

def main():
    a = float(input('Please enter a number: '))
    b = float(input('Please enter a number: '))
    c = float(input('Please enter a number: '))


    sol_1, sol_2 = quadratic(1,2,1)
    
    if sol_1 is not None:
        print(f"The roots of the equation are {sol_1} and {sol_2}.")
    else:
        print('No real number solutions.')

if __name__ == "__main__":
    main()
    
    
#solve 1*x**2 + 2 * x + 1 = 0 
#expected -1, -1







    
    

