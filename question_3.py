n=int(input('Enter the the integer value: '))
if n%4==0:
    if n%100==0 and n%400!=0:
        print('The given integer %d doesnot correspond to a leap year' % n)
    elif n%100==0 and n%400==0:
        print('The given integer %d does correspond to a leap year' % n)
    else:
        print('The given integer %d does correspond to a leap year' % n)

else:
    print('The given integer %d doesnot correspond to a leap year'%n)
    