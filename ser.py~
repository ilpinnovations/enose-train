import serial
import pandas as pd
from sklearn.linear_model import LogisticRegression
import time 
import ast

reg = LogisticRegression()
df = pd.read_csv("normal.csv")
x = df[[u'sen1',u'sen2',u'sen3',u'sen4',u'sen5']]
y = df[[u'value']]
# print(type(y))
reg.fit(x,y)
# print(reg)

ser = serial.Serial(
    port='/dev/ttyACM0',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0.1)

print("connected to: " + ser.portstr)

line = ""
while True:
    for c in ser.readline():
        line=line + c
        if c == '\n': 
            t = line.split('\r\n')[0].split(' ')
            print(t)
            try:
                if(reg.predict(map(ast.literal_eval,t)) == 4):
                    print("Marker")
                elif (reg.predict(map(ast.literal_eval,t)) == 3):
                    print("Chilly")
                elif (reg.predict(map(ast.literal_eval,t)) == 2):
                    print("PineApple")
                elif (reg.predict(map(ast.literal_eval,t)) == 1):
                    print("Orange")
                elif (reg.predict(map(ast.literal_eval,t)) == 0):
                    print("Nothing is present")
    
            except Exception, e:
                pass
            
            # time.sleep(1)
            line = ""
            break
	    
ser.close()
