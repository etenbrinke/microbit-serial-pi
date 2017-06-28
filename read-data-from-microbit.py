import serial

# Open the serial port for sending at speed 115200 bits/second
PORT = "/dev/ttyACM0"
BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

try:
    while True:
        # Read data from serial port, decode it and strip whitespaces 
        data = s.readline().rstrip()

        # Split the accelerometer and button data into x, y, z, a, b
        data_s = data.split(" ")
        x, y, z = data_s[0], data_s[1], data_s[2]
        a, b = data_s[3], data_s[4]
        print(x,y,z,a,b)

# Close serial port
finally:
    s.close()

