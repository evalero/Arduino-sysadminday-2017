import serial
import time
import pygame.mixer
from pygame.mixer import Sound

arduino = serial.Serial('/dev/ttyACM0', 9600)
# Dejamos los 5 milis de rigor para que se inicialice el puerto serie
time.sleep(5)
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
dale = Sound('./sounds/dale.wav')
dale_mas = Sound('./sounds/dale_mas.wav')
vale = Sound('./sounds/vale.wav')
da_un_parte = Sound('./sounds/daunparte.wav')


def recibe_datos():
    entrada = float(arduino.readline())
    if (entrada > 1000.0):
        print ("Te has pasado")
        print (entrada)
        da_un_parte.play()
    elif (entrada > 10.0 and entrada < 1000.0):
        print ("dale mas")
        print (entrada)
        dale_mas.play()
    elif (entrada > 4 and entrada < 1000.0):
        print ("mas")
        print (entrada)
        dale.play()
    elif (entrada < 3):
        print ("vale!")
        print (entrada)
        vale.play()


try:
    while True:
        recibe_datos()
except KeyboardInterrupt as e:
    arduino.close()
    print "saliendo ordenadamente"
