# Andrew Bowman 2024
# RP2040 Macro Keyboard V1

# You must have macros.txt on your CIRCUITPY drive for this to work.

import time
import board
import digitalio
import simpleio
from digitalio import DigitalInOut, Direction, Pull
import time
import busio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
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
        
    keyboard.release_all()
    time.sleep(0.1);

