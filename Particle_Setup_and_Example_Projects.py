/*
 * Project assignment_3
 * Description:
 * Author:
 * Date:
 */
#include "Grove_Temperature_And_Humidity_Sensor.h"
DHT dht(D2);

float temp, humidity;
double temp_dbl, humidity_dbl;
temp_dbl = temp;
humidity_dbl = humidity;

// setup() runs once, when the device is first turned on.
void setup()
{
Serial.begin(9600);

dht.begin();
}

Particle.variable("temp", temp_dbl);
Particle.variable("humidity", humidity_dbl);

// loop() runs over and over again, as quickly as it can execute.
void loop()
{
float temp, humidity;

temp = dht.getTempFarenheit();
humidity = dht.getHumidity();

Serial.printlnf("Temp: %f", temp);
Serial.printlnf("Humidity: %f", humidity);

delay(10000);
}

//###  Light
#include "Grove_ChainableLED.h"
ChainableLED leds(A4, A5, 1);

// setup() runs once, when the device is first turned on.
void setup()
{
  

}
// setup() runs once, when the device is first turned on.
void setup()
{
leds.init();
leds.setColorHSB(0, 0.0, 0.0, 0.0);
}

int toggleLed(String args) {
  leds.setColorHSB(0, 0.0, 1.0, 0.5);

delay(500);

leds.setColorHSB(0, 0.0, 0.0, 0.0);

toggleLed("");

