long tiempo;
int disparador = 7;   // triger
int entrada = 8;      // echo
float distancia;

void setup()
{
  pinMode(disparador, OUTPUT);
  pinMode(entrada, INPUT);
  
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
  //tomamos muestras cada segundo
  delay(1000);
}
