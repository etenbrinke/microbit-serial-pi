import serial

# serial port on raspberry pi will probably be /dev/ttyACM0
PORT = "/dev/ttyACM0"

BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

try:
    while True:
        # read a line from the microbit and decode it
        data = s.readline().decode('UTF-8')

        # strip whitespaces and split the accelerometer and button data into x, y, z, a, b
        data_s = data.rstrip().split(' ')
        x, y, z = data_s[0], data_s[1], data_s[2]
        a, b = data_s[3], data_s[4]
        print(x,y,z,a,b)

finally:
    s.close()

