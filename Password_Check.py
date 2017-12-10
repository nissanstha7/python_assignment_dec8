#!/usr/bin/python3
global code
code='How you doing?'

def check_code():
    password=input('Enter the password: ')
    if password==code:
        print('Password match.')
    else:
        print('Wrong password.')

check_code()
