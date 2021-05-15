import socket
from serial import Serial
import threading, queue

records = queue.Queue()
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
serverAddressPort = ("192.168.1.33", 20001)
bufferSize = 1024
ser = Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()


def communicate_with_server():
	while True:
#		server_message = UDPClientSocket.recvfrom(bufferSize)
		print("sent something to server")
		UDPClientSocket.sendto(records.get().encode(), serverAddressPort)
#		elif server_message is not "":
#			if server_message is "pump":
#				print("pump activated")

def get_sensors_message():
	while True:
		if ser.in_waiting > 0:
			line = ser.readline().decode('utf-8').rstrip()
			print(line + "inserted")
			records.put(line)


sensorthread = threading.Thread(target=get_sensors_message)
communicationThread = threading.Thread(target=communicate_with_server)

sensorthread.start()
communicationThread.start()

