from ctypes import *

def isComputerLocked():
    u = windll.LoadLibrary('user32.dll')
    result = u.GetForegroundWindow()
    if result % 10 == 0:
        return True
    return False

def countTheTimeOfLock():
    global lockedTime
    lockedTime = 0
    while True:
        if isComputerLocked():
            lockedTime += 1
        else:
            break
    return lockedTime

if __name__ == '__main__':
    if isComputerLocked():
        print('Locked')
    else:
        print('Not locked')