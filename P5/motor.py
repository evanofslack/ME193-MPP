# Evan Slack 
# Motor control through PIO on the Pico

from time import sleep
from machine import Pin, PWM
from rp2 import PIO, StateMachine, asm_pio

# Def pins for motor control
motorA = Pin(14, Pin.OUT)
motorB = Pin(15, Pin.OUT)
standby = Pin(12, Pin.OUT)
standby.high()

max_count = 1000 
count_freq = 10000000


class pioPWM:
    def __init__(self, sm_id, pin, max_count, count_freq):
        self._sm = StateMachine(sm_id, pwm_prog, freq=count_freq, sideset_base=Pin(pin))
        self._sm.put(max_count)
        self._sm.exec("pull()")
        self._sm.exec("mov(isr, osr)")
        self._sm.active(1)
        self._max_count = max_count

    def set(self, value):
        value = max(value, -1)
        value = min(value, self._max_count)
        self._sm.put(value)

# Set PIO
@asm_pio(sideset_init=PIO.OUT_LOW) # Defines as asm
def pwm_prog():
    pull(noblock) .side(0)
    mov(x, osr) # Take osr to x
    mov(y, isr) # Take isr to y
    label("pwmloop")
    jmp(x_not_y, "skip")
    nop()         .side(1)
    label("skip")
    jmp(y_dec, "pwmloop")


# Initialize State Machine
pwmStateMach = pioPWM(0,13, max_count, count_freq)

# Define Motor Movements
def forward():
   motorA.high()
   motorA.low()
   
def backward():
    motorA.low()
    motorB.high()

def stop():
   motorA.low()
   motorB.low()
   
def run():
    forward()
    pwm.duty_u16(1000)

def jerky():
    forward()
    pwm_StateMach.set(1000)
    sleep(2)
    stop()
    
def smooth():
    forward()
    for i in range(100, 1000, 10):
        velocity = int(0.0001*(i*i))
        pwm_StateMach.set(velocity)
        sleep(0.001)
    stop()
    
# Execute    
if __name__ == "__main__":
    print("Jerky Acceleration")
    jerky()
    
    sleep(5)
    
    print ("Smooth Acceleration")
    smooth()
    





