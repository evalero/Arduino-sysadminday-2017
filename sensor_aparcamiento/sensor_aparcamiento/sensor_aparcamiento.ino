#include "pitches.h"
long tiempo;
int disparador = 7;   // trigger
int entrada = 8;      // echo
float distancia;
int altavoz = 2;

void setup()
{
  pinMode(disparador, OUTPUT);
  pinMode(entrada, INPUT);
  pinMode(altavoz, OUTPUT);
  Serial.begin(9600);
}


void loop()
{
  // lanzamos un pequeño pulso para activar el sensor
  digitalWrite(disparador, HIGH);
  delayMicroseconds(10);
  digitalWrite(disparador, LOW);
  
  // lanzamos el pulso y esperamos que nos devuelva un HIGH para leer el valor del tiempo tardado
  tiempo = (pulseIn(entrada, HIGH)/2); 
  // Este tiempo debe ser dividido entre 2, ya que es la ida y la vuelta del ultrasonido
                                       
  // ahora calcularemos la distancia en cm
  // sabiendo que el espacio es igual a la velocidad por el tiempo
  // y que la velocidad del sonido es de 343m/s y que el tiempo lo 
  // tenemos en millonesimas de segundo
  distancia = float(tiempo * 0.0343);
  // La distancia es el tiempo * la velocidad del sonido (343 m/s),
  // hay que tener en cuenta que el tiempo es en microsegundos
  // y lo mostramos por el puerto serie una vez por segundo
  Serial.println(distancia);
  if (distancia > 1000 || distancia < 3){
    Serial.println(distancia);
    tone(altavoz,NOTE_B5,1000);
    delay(1000);
  }
    else if (distancia <= 300.0 and distancia > 5){
      Serial.println(distancia);
      tone (altavoz, NOTE_C5, 20);
      delay (2000);
    }
    else if (distancia <= 5 and distancia > 3){
      Serial.println(distancia);
      tone (altavoz, NOTE_D5, 100);
      delay(1000);
    }
    else {
     Serial.println(distancia);
     noTone(altavoz);
  }
     
  
  
}
