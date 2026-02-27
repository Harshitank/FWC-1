from machine import Pin
import time

led = Pin(15, Pin.OUT)

a = Pin(4, Pin.OUT)
b = Pin(5, Pin.OUT)
c = Pin(6, Pin.OUT)
d = Pin(7, Pin.OUT)
e = Pin(8, Pin.OUT)
f = Pin(9, Pin.OUT)
g = Pin(10, Pin.OUT)

minterms = [0,1,3,5,9,10,14]

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
        a.value(val[0])
        b.value(val[1])
        c.value(val[2])
        d.value(val[3])
        e.value(val[4])
        f.value(val[5])
        g.value(val[6])

while True:
    for num in range(16):
        
        
        display_digit(num % 10)
        led.value(0)
        time.sleep(1)

        
        if num in minterms:
            display_digit(1)
            led.value(1)
        else:
            display_digit(0)
            led.value(0)
            
        time.sleep(1)