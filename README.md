# Communication between the micro:bit and the Raspberry Pi via serial USB device

apt-get install python-serial

## Files

- read-data-from-pi.py		- Python3 program runs on the Pi and reads the data coming from the Microbits USB connection 
- write-data-to-serial.py	- MicroPython program runs on micro:bit and write accelerometer and button data to Microbits USB connection

On the Pi you need to install the packages python-serial and python3-serial using the apt package manager
```
sudo apt-get install python3-serial
```

Now you can import the module from both Python 2 and 3 with the name ```serial```:
```
python3 -c "import serial; print(serial.__file__)"
```

If this command show you the file where the serial module is located, it works correctly.
