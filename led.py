import pyfirmata 
PORT = "/dev/ttyUSB0"
BOARD = pyfirmata.Arduino(PORT)

def onLed(pos=13):
    BOARD.digital[pos].write(1)

def offLed(pos):
    BOARD.digital[pos].write(0)
