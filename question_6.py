import math# import math module since we need to evaluate e
P=float(input('Enter the principal :$'))#P variable stores the principal entered
t=int(input('Enter the years :')) #t variable stores the number of years
r=float(input('Enter the interest rate:'))# r variable stores the interest rate, it has to entered in decimal not in percentage
def desiredvalue(P,t,r):#defining desired value which depends upon P,t,r variables
    z=r*t# #evaluating the interest rate multiplied by time t stored in variable z
    i=math.e**z #evaluating exponential of z
    return P*i # returns the value of principal multiplied by variable i
a=desiredvalue(P,t,r) #assigning the return value to variable a
print('The amount of money you will have if invested %d at interest rate %.4f for %d year is $%.2f'%(P,r,t,a))

