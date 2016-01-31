import serial
from time import sleep
ser = serial.Serial('/dev/ttyACM0', 9600)

#serial port likes to be tickled once before it responds to each call
ser.readline()
ser.readline()

# forward=1, reverse=2, turn=3, stop=0
ser.write("p1,250")
sleep(3)
ser.write("p0,255")
