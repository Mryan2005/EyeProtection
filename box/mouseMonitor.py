import win32api
import numpy as np
import time

# is the mouse moved?
def isMoved():
    global lastPos
    pos = np.array(win32api.GetCursorPos())
    if np.array_equal(lastPos, pos):
        return False
    lastPos = pos
    return True

if __name__ == '__main__':
    lastPos = np.array(win32api.GetCursorPos())
    while True:
        time.sleep(1)
        if isMoved():
            print('Moved')
        else:
            print('Not moved')