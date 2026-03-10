import numpy as np
import time

led = 0

a=b=c=d=e=f=g=0

minterms = np.array([0,1,3,5,9,10,14])

def display_digit(num):

    digits = {
        0:(0,0,0,0,0,0,1),
        1:(1,0,0,1,1,1,1),
        2:(0,0,1,0,0,1,0),
        3:(0,0,0,0,1,1,0),
        4:(1,0,0,1,1,0,0),
        5:(0,1,0,0,1,0,0),
        6:(0,1,0,0,0,0,0),
        7:(0,0,0,1,1,1,1),
        8:(0,0,0,0,0,0,0),
        9:(0,0,0,0,1,0,0)
    }

    if num in digits:
        val = digits[num]
        print("Segments:",val)

while True:

    for num in range(16):

        display_digit(num % 10)
        led = 0
        print("LED:",led)

        time.sleep(1)

        if num in minterms:
            display_digit(1)
            led = 1
        else:
            display_digit(0)
            led = 0

        print("LED:",led)

        time.sleep(1)