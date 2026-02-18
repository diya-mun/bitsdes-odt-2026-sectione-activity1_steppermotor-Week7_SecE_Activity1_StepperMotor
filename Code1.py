from machine import Pin
import time
time = 0.05

wave = [[1.0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

in1 = Pin(14,PIN.OUT)
in2 = Pin(25,PIN.OUT)
in3 = Pin(26,PIN.OUT)
in4 = Pin(27,PIN.OUT)

while True :
    for i in wave:
        in1.value(i[1])
        in2.value(i[2])
        in3.value(i[3])
        in4.value(i[4])
        
        time.sleep(time)
        
        in1.value(i[1])
        in2.value(i[2])
        in3.value(i[3])
        in4.value(i[4])
        
        time.sleep(time)
        
        in1.value(i[1])
        in2.value(i[2])
        in3.value(i[3])
        in4.value(i[4])
        
        time.sleep(time)
        
        in1.value(i[1])
        in2.value(i[2])
        in3.value(i[3])
        in4.value(i[4])
        
        
        
        
        
        
