import pyautogui
import time


# Run script and point the mouse and hold 5 seconds to get a pyautogui Point() position on the screen
def get_mouse_position():
    time.sleep(5)
    return pyautogui.position()


print(get_mouse_position())
