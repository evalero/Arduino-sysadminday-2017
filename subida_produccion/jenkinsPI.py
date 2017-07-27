import RPi.GPIO as GPIO
import time
import jenkins

server = jenkins.Jenkins('http://192.168.1.134:8889',username='admin', password='admin')
user = server.get_whoami()
print " Hello %s from jenkins " % (user['fullName'])
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
contador = 0

while contador < 20:
    input19 = GPIO.input(19)
    if input19 == 1:
        server.build_job('Raspberry To Production Ok')

    print 'La salida de la entrada 19 es %s y el contador %s' % (input19,
                                                                 contador)
    contador += 1
    time.sleep(1)
