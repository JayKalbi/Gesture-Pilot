import keyboard
import time

# Virtual key names (using keyboard library names)
up_pressed = 'up'
down_pressed = 'down'
right_pressed = 'right'
left_pressed = 'left'

def KeyOn(key):
    keyboard.press(key)

def KeyOff(key):
    keyboard.release(key)

if __name__ == '__main__':
    while True:
        KeyOn(up_pressed)
        time.sleep(1)
        KeyOff(up_pressed)
        time.sleep(1)
