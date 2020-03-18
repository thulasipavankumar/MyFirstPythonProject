import pynput
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
while (True):
    time.sleep(15.4)
    keyboard.press(Key.space)
    keyboard.release(Key.space)