# if/while condition

import sys


playTimes = 5

while playTimes != 0:

    stringInput = input('Please enter a number:')
    numInput = int(stringInput)

    if numInput > 100:
        print('the number is bigger than 100')
    elif numInput < 0:
        print('the number is smaller than 0')
    else:
        print('the number is between 0 and 100')

    playTimes = playTimes - 1
else:
    print('END')
