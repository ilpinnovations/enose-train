import serial
import ast

ser = serial.Serial(
    port='/dev/ttyACM1',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)

line = ""
while True:
    for c in ser.readline():
        if c == '\n': 
            # t = line.split('\r\n')[0].split(' ')
            # print(map(ast.literal_eval, t))
            print(line)
            line = ""
            break
        line=line + c
	    
ser.close()