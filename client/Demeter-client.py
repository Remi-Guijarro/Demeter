import socket
from serial import Serial

serverAddressPort = ("192.168.1.33", 20001)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
ser = Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()
while True:
	if ser.in_waiting > 0:
		line = ser.readline().decode('utf-8').rstrip()
		UDPClientSocket.sendto(line.encode(), serverAddressPort)


