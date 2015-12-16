"""
This is for adding two Numbers by taking input from User
"""


def add_num(arg1, arg2):
    try:
        add = int(arg1) + int(arg2)
        print 'The Sum of ', arg1, ' and ', arg2, ' is: ', add

    except Exception, err:
        print 'Error while adding : ', err


def take_input():
    arg1 = raw_input('Please enter first No : ')
    arg2 = raw_input('Please enter second No : ')

    add_num(arg1, arg2)


take_input()
