# Andrew Bowman 2024
# RP2040 Macro Keyboard V2

# You must have macros.txt on your CIRCUITPY drive for this to work.
# Rotary Encoder https://learn.adafruit.com/rotary-encoder/circuitpython
import time
import board
import digitalio
import simpleio
from digitalio import DigitalInOut, Direction, Pull
import time
import rotaryio
import busio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import array as arr

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Define the input pins
io0 = digitalio.DigitalInOut(board.GP0)
io1 = digitalio.DigitalInOut(board.GP1)
io2 = digitalio.DigitalInOut(board.GP2)
io3 = digitalio.DigitalInOut(board.GP3)
io4 = digitalio.DigitalInOut(board.GP4)
io5 = digitalio.DigitalInOut(board.GP5)
io6 = digitalio.DigitalInOut(board.GP6)
io7 = digitalio.DigitalInOut(board.GP7)
io8 = digitalio.DigitalInOut(board.GP8)
io9 = digitalio.DigitalInOut(board.GP9)
io10 = digitalio.DigitalInOut(board.GP10)
io11 = digitalio.DigitalInOut(board.GP11)
io12 = digitalio.DigitalInOut(board.GP12)
io13 = digitalio.DigitalInOut(board.GP13)
io14 = digitalio.DigitalInOut(board.GP14)
io15 = digitalio.DigitalInOut(board.GP15)
io26 = digitalio.DigitalInOut(board.GP26)
encoder = rotaryio.IncrementalEncoder(board.GP27, board.GP28)

io0.pull = Pull.UP # define buttons as pull ups
io1.pull = Pull.UP
io2.pull = Pull.UP
io3.pull = Pull.UP
io4.pull = Pull.UP
io5.pull = Pull.UP
io6.pull = Pull.UP
io7.pull = Pull.UP
io8.pull = Pull.UP
io9.pull = Pull.UP
io10.pull = Pull.UP
io11.pull = Pull.UP
io12.pull = Pull.UP
io13.pull = Pull.UP
io14.pull = Pull.UP
io15.pull = Pull.UP
io26.pull = Pull.UP

cc = ConsumerControl(usb_hid.devices)
enc_button_state = None
enc_last_button_state = None
press_count = 0
last_press_time = time.monotonic()
last_position = encoder.position
DEBOUNCE_TIME = 0.2 # seconds
button_state = False
double_press_time = 0.4

with open('macros.txt', 'r') as file: # Parse macros.txt for each line
    for line in file:
        if '00:' in line:
            text0 = line.split('00:')[1].strip()  # Sets text0 equal to the first line of the fule after 00:
        if '01:' in line:
            text1 = line.split('01:')[1].strip()
        if '02:' in line:
            text2 = line.split('02:')[1].strip()
        if '03:' in line:
            text3 = line.split('03:')[1].strip()
        if '04:' in line:
            text4 = line.split('04:')[1].strip()
        if '05:' in line:
            text5 = line.split('05:')[1].strip()
        if '06:' in line:
            text6 = line.split('06:')[1].strip()
        if '07:' in line:
            text7 = line.split('07:')[1].strip()
        if '08:' in line:
            text8 = line.split('08:')[1].strip()
        if '09:' in line:
            text9 = line.split('09:')[1].strip()
        if '10:' in line:
            text10 = line.split('10:')[1].strip()
        if '11:' in line:
            text11 = line.split('11:')[1].strip()
        if '12:' in line:
            text12 = line.split('12:')[1].strip()
        if '13:' in line:
            text13 = line.split('13:')[1].strip()
        if '14:' in line:
            text14 = line.split('14:')[1].strip()
        if '15:' in line:
            text15 = line.split('15:')[1].strip()

while True:
    if not io0.value: # if io0.value is low, then type text0
        layout.write(text0)
    if not io1.value:
        layout.write(text1)
    if not io2.value:
        layout.write(text2)
    if not io3.value:
        layout.write(text3)
    if not io4.value:
        layout.write(text4)
    if not io5.value:
        layout.write(text5)
    if not io6.value:
        layout.write(text6)
    if not io7.value:
        layout.write(text7)
    if not io8.value:
        layout.write(text8)
    if not io9.value:
        layout.write(text9)
    if not io10.value:
        layout.write(text10)
    if not io11.value:
        layout.write(text11)
    if not io12.value:
        layout.write(text12)
    if not io13.value:
        layout.write(text13)
    if not io14.value:
        layout.write(text14)
    if not io15.value:
        layout.write(text15)
        
    current_position = encoder.position
    position_change = current_position - last_position
    enc_button_state = None
    
    if not io26.value and enc_button_state is None:
        enc_button_state = "pressed"

    
    if position_change > 0 and enc_button_state == None:
        for _ in range(position_change):
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        print(current_position)
    elif position_change < 0 and enc_button_state == None:
        for _ in range(-position_change):
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        print(current_position)
    elif position_change > 0 and enc_button_state == "pressed":
        print("Next Track")
        for _ in range(position_change):
            cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        print(current_position)
        time.sleep(2)
    elif position_change < 0 and enc_button_state == "pressed":
        print("Prev Track")
        for _ in range(-position_change):
            cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
        print(current_position)
        time.sleep(2)

    current_time = time.monotonic()

    if not io26.value and not button_state:
        button_state = True
        if current_time - last_press_time < double_press_time :
            press_count = press_count + 1
        else:
            press_count = 1
        last_press_time = current_time
        
    if io26.value and button_state:
        button_state = False
        
    if press_count == 1 and current_time - last_press_time >= double_press_time:
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        press_count = 0
    elif press_count == 2:
        cc.send(ConsumerControlCode.MUTE)
        press_count = 0
        
    last_position = current_position
          
    keyboard.release_all()
    time.sleep(0.05);

