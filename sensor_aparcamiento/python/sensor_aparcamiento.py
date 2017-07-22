import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 9600)
# Dejamos los 5 milis de rigor para que se inicialice el puerto serie
time.sleep(5)


def recibe_datos():
    entrada = float(arduino.readline())
    if (entrada > 1000.0):
        print ("Te has pasado")
        print (entrada)
    elif (entrada > 10.0 and entrada < 1000.0):
        print ("dale mas")
        print (entrada)
    elif (entrada > 4 and entrada < 1000.0):
        print ("mas")
        print (entrada)
    elif (entrada < 3):
        print ("vale!")
        print (entrada)


while True:
    recibe_datos()
