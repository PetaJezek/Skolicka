from datetime import datetime
import random

dataRegister = 0
statusRegister = 0
print("Note: original 8250A RS-232 controller would reset with both RTS and DTR set to OFF.")
print("      This simulated 8250A resets both RTS and DTR to ON for educational purposes.")
print("      The simulated RS-232 mouse requires reset to start working properly - also for educational purposes.")
modemControlRegister = 0x03 # = 0x00 to simulate correct 8250A reset behavior
mouseAfterReset = False

startTime = datetime.now()
inputEvents = []

def setSimulatedInputEvents(simulatedInputEvents):
    global inputEvents
    inputEvents = simulatedInputEvents

def _tryReceiveData():
    global inputEvents, statusRegister, dataRegister

    if len(inputEvents) > 0:
        if modemControlRegister == 0 or not mouseAfterReset:
            return    # Both DTR and RTS are off, so simulate the mouse without power
        if statusRegister == 0:     # Simulate input buffer, so no data bytes are lost
            nextEvent = inputEvents[0]
            currentDelta = datetime.now() - startTime
            if nextEvent[0] < currentDelta:
                inputEvents.pop(0)
                if modemControlRegister != 0x03:
                    dataRegister = random.randint(0, 255)   # One of DTR or RTS is off, so simulate mouse not fully powered generating random data
                else:
                    dataRegister = nextEvent[1]
                statusRegister = 1

def readDataRegister(controllerId):
    global statusRegister, dataRegister

    _tryReceiveData()
    
    statusRegister = 0
    return dataRegister

def readStatusRegister(controllerId):
    global statusRegister

    _tryReceiveData()
    
    return statusRegister

def readModemControlRegister(controllerId):
    global modemControlRegister

    return modemControlRegister

def writeModemControlRegister(controllerId, byteValue):
    global modemControlRegister
    global mouseAfterReset

    modemControlRegister = byteValue
    print("RS-232 line state changed to: | RTS", "OFF" if modemControlRegister & 0x02 == 0 else "+5V", "| DTR", "OFF" if modemControlRegister & 0x01 == 0 else "+5V", "|")
    if modemControlRegister == 0:
        mouseAfterReset = True
