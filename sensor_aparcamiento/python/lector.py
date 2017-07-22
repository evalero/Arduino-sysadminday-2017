import serial
import time
import pygame.mixer
from pygame.mixer import Sound

arduino = serial.Serial('/dev/ttyACM0', 9600)
# Tiempo de espera para que pueda inicializar el puerto serie
time.sleep(5)
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
# rigoletto = Sound("./sounds/Rigoletto.wav")
# gun = Sound('./sounds/Pistol.wav')


def lanzarEscena(escena):
    procesado = True
    tipo = type(escena)
    print "Lanzando escena %r %s" % (escena, tipo)
    play(escena)
    arduino.write(escena)
    while (procesado):
        print ("entrando en el bucle")
        entrada = arduino.readline()
        print(entrada)
        procesado = False
    stop(escena)
    return True


def play(escena):
    if (escena == '1'):
        print "lanzando el Rigoletto"
        rigoletto.play()
    elif (escena == '2'):
        print "lanzando el disparo"
        gun.play()

def stop(escena):
    if (escena == '1'):
        "parando el Rigoletto"
        rigoletto.stop()
    elif (escena == '2'):
        "parando el disparo"
        gun.stop()


# MAIN
try:
    while True:
        lanzarEscena('1')
        lanzarEscena('2')
except KeyboardInterrupt as e:
    arduino.close()
    print "saliendo ordenadamente"
