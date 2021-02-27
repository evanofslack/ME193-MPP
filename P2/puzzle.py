# Evan Slack
# Raspberry Pi Oscilliscope Puzzle
# Feb 27th 2021

from machine import Pin 
from time import sleep

# Initialize Pins
led = Pin(25, Pin.OUT)
signal = Pin(12,Pin.OUT)

# Initialize morse code dictionary
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
                    
# Converts letters into morse code dots and dashes
def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            # 1 space indicates different characters 
            # and 2 indicates different words 
            cipher += ' '
  
    return cipher 
    
# Converts "." and "-" into time delayed pulses to be sent to the GPIO pins    
def transmit(cipher)
    for charecter in cipher:
        if charecter == '.': # Short pulse
            signal.value(1)
            sleep(0.1)
            signal.value(0)
            sleep(0.1)
        if charecter == '-': # Long Pulse
            signal.value(1)
            sleep(0.3)
            signal.value(0)
            sleep(0.1)
        if charecter == ' ': # Longer pulse to indicate new letter
            i +=
            signal.value(0)
            sleep(0.5)
        
            
#functions for LED states
def stage1():
    led.value(1)
    sleep(0.1)
    led.value(0)
    #sleep(0.9)
    
def stage2():
    led.value(1)
    sleep(0.1)
    led.value(0)
    sleep(0.1)
    led.value(1)
    sleep(0.1)
    led.value(0)
    #sleep(0.8)
        
def stage3():
    led.value(1)
    sleep(0.1)
    led.value(0)
    sleep(0.1)
    led.value(1)
    sleep(0.1)
    led.value(0)
    sleep(0.1)
    led.value(1)
    sleep(0.1)
    led.value(0)
    #sleep(0.7)
    
def stage_solved():
    led.value(1)
    sleep(0.1)
    led.value(0)
    sleep(0.1)

while stage1 = True:
    stage1() # Blink the LED
    
    input = input("Enter \"m\" to get morse code message on pin 12, or enter the decoded message to proceed")
    
    if input == "m":
        signal = encrypt("brandon")
        transmit(signal)
    elif input == "brandon":
        print("Correct, proceeding to stage 2")
        stage1 = False
        #break
    else:
        print("Incorrect message")
        stage1()
        
while stage2 = True:
    stage2() # Blink the LED
    
    input = input("Enter \"m\" to get morse code message on pin 12, or enter the decoded message to proceed")
    
    if input == "m":
        signal = encrypt("gary")
        transmit(signal)
    elif input == "gary":
        print("Correct, proceeding to stage 3")
        stage2 = False
        #break
    else:
        print("Incorrect message")
        stage2()

while stage3 = True:
    stage3() # Blink the LED
    
    input = input("Enter \"m\" to get morse code message on pin 12, or enter the decoded message to proceed")
    
    if input == "m":
        signal = encrypt("felix")
        transmit(signal)
    elif input == "felix":
        print("Correct, you've solved the puzzle!")
        print("Here is the celebratory hash: ")
        print ("ac46d94a097a6bad39fbcf0073ce57cf12d917d30af560403e82faef6d2c030a")
        stage3 = False
        #break
    else:
        print("Incorrect message")
        stage3()
        
while True:
    stage_solved()
           