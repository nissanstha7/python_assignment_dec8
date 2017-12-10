#!/usr/bin/python3

def check_even(num):
    if num%2==0:
        return 1

    else:
        return 0


num=int(input('Enter a number: '))

flag=check_even(num)

if flag==1:
    print('The number {} is even.'.format(num))
else:
    print('The number {} is odd.'.format(num))
    
