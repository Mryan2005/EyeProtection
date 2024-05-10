from ctypes import *

def isComputerLocked():
    u = windll.LoadLibrary('user32.dll')
    result = u.GetForegroundWindow()
    if result % 10 == 0:
        return True
    return False

if __name__ == '__main__':
    if isComputerLocked():
        print('Locked')
    else:
        print('Not locked')