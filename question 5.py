import sys
m=int(sys.argv[1]) #enter the month
d=int(sys.argv[2]) #enter the day
import datetime # imported datetime module
try: #to check if the month and day value entered is valid one or not
    datetime.datetime(2016,m,d)#used 2016 as reference year to chech day and month
    x = False  # assigning x as false to use in loop
    if m == 3: #this if loop checks if the entered month value is march
        if d > 19: #checks if the day value is above 19
            x = True #then x is assigned true
            print(x) # prints the x value
        else:
            print(x)#otherwise if d value is less than 20 x is printed which is false
    elif m > 3 and m < 6: # performs the below expression if month value is 4or5
        x = True #x is assigned true
        print(x)#prints true for all valid date values
    elif m == 6: #performs the below expression if m value is 6
        if d < 21:#checks if the day value entered if 21
            x = True #x becomes true
            print(x)#prints true for those values of d and m
        else:
            print(x) #if not it prints false
    else:
        print(x) # if the entered value does not belong form 3 to 6 below expresson is done
except ValueError:#if invalid day and month value is entered it prints invalid day and month
    print("invalid day and month")

