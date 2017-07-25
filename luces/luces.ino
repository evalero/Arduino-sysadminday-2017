int outMin = 8;
int outMax = 13;

void setup() {
  //init lights located from pin 8 to 13
  for (int i = outMin; i <= outMax; i++) {
    pinMode(i, OUTPUT);
  }
  //if analog input pin 0 is unconnected, is a good seed
  // seen https: //www.arduino.cc/en/Reference/Random
  randomSeed(analogRead(0));
  Serial.begin(9600);
  for (int i = outMin; i <= outMax; i++) {
    digitalWrite(i, random(0, 2));
  }


}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite (random(outMin,outMax+1),random(0,2));
  delay(random(5000, 20000));


}
