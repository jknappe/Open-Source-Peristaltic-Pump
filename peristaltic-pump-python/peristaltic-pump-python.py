import serial
import time
import msvcrt

print("")
print("+ ======================================== +")
print("+               ARDUINO PUMP               +")
print("+ ======================================== +")
print("")
print("Author: jan.knappe@tcd.ie")
print("")
print("Press 'q' to terminate the program.")
print("")
print("+ ======================================== +")
print("")
print("Establishing serial connection...")
print("")
COM3 = serial.Serial('COM3', 9600, timeout = 1)
print("COM3: Conection Established!")
COM4 = serial.Serial('COM4', 9600, timeout = 1)
print("COM4: Conection Established!")
COM5 = serial.Serial('COM5', 9600, timeout = 1)
print("COM5: Conection Established!")
print("")
time.sleep(1)
print("+ ======================================== +")
print("")
print("You have 5 seconds to enable USB communication on the Arduino Pumps.")
time.sleep(1)
for i in range(5):
	print(10 - i, "..")
	time.sleep(1)
print("")
print("+ ======================================== +")
time.sleep(2)

while 1:
	
	command = 'd200,60000,20000'
	COM4.write(command.encode())
	print("request_dose,200,60000,NA")
	arduinoData = COM4.readline().decode('ascii')
	print(arduinoData)
	
	time.sleep(5)
	
	if msvcrt.kbhit():
		keypress = ord(msvcrt.getch())
		if keypress == 113: #== q
			break
			

print("+ ======================================== +")
print("Program stopped.")
print("+ ======================================== +")