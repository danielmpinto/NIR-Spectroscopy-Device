/*
  ReadAnalogVoltage

  Reads an analog input on pin 0, converts it to voltage, and prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/ReadAnalogVoltage
*/
#include <Arduino.h>
#include <Wire.h>
#include <LiquidCrystal_PCF8574.h>

#define RGB_RED 2
#define RGB_GREEN 3
#define RGB_BLUE 4
#define buzzer 5

LiquidCrystal_PCF8574 lcd(0x27);  // set the LCD address to 0x27 for a 16 chars and 2 line display

byte dotOff[] = { 0b00000, 0b01110, 0b10001, 0b10001,
                  0b10001, 0b01110, 0b00000, 0b00000 };
byte dotOn[] = { 0b00000, 0b01110, 0b11111, 0b11111,
                 0b11111, 0b01110, 0b00000, 0b00000 };

// loading initial
void loading(){
  lcd.setBacklight(255);
  lcd.home();
  lcd.clear();
  lcd.print("Iniciando. ");
  digitalWrite(RGB_RED, 1);
  delay(500);
  digitalWrite(RGB_RED, 0);
  delay(500);
  lcd.clear();
  lcd.print("Iniciando.. ");
  digitalWrite(RGB_RED, 1);
  delay(500);
  digitalWrite(RGB_RED, 0);
  delay(500);
  lcd.clear();
  lcd.print("Iniciando... ");
  digitalWrite(RGB_RED, 1);
  delay(500);
  digitalWrite(RGB_RED, 0);
  delay(500);
  lcd.clear();
  lcd.print("Iniciando.... ");
  digitalWrite(RGB_RED, 1);
  delay(500);
  digitalWrite(RGB_RED, 0);
  delay(500);
  lcd.clear();
  lcd.print("Tudo pronto!");
  musicaInicio();

  

  

  digitalWrite(RGB_GREEN, 1);
  delay(1000);
}

void tocarNota(int frequencia, int duracao) {
  tone(buzzer, frequencia, duracao);
  delay(duracao + 50); // Adiciona um pequeno atraso entre as notas
}

void musicaInicio() {
  // Notas musicais (frequências) para uma escala maior
  int C = 261;
  int E = 329;
  int G = 392;

  // Define a sequência de notas para a música de boas-vindas
  tocarNota(G, 300);
  tocarNota(E, 300);
  tocarNota(C * 2, 600);
}

void musicaFim() {
  // Notas musicais (frequências) para uma escala maior
  int C = 261;
  int E = 329;
  int G = 392;

  // Define a sequência de notas para a música de boas-vindas
  tocarNota(C * 2, 600);
  tocarNota(E, 300);
  tocarNota(G, 300);
  
  
}

void musicaMedir() {
  // Notas musicais (frequências) para uma escala maior
  int E = 329;

  // Define a sequência de notas para a música de boas-vindas
  tocarNota(E, 300);
  
  
}



                
// the setup routine runs once when you press reset:
void setup() {
  pinMode(RGB_BLUE, OUTPUT);
  pinMode(RGB_RED, OUTPUT);
  pinMode(RGB_GREEN, OUTPUT);
  pinMode(buzzer, OUTPUT);
  Serial.begin(115200);
  Serial.println("LCD...");

  // See http://playground.arduino.cc/Main/I2cScanner how to test for a I2C device.
  Wire.begin();
  Wire.beginTransmission(0x27);

  lcd.begin(16, 2);  // initialize the lcd

  lcd.createChar(1, dotOff);
  lcd.createChar(2, dotOn);
  loading();
}


void medicao(){
  digitalWrite(RGB_GREEN, 0);  
  digitalWrite(RGB_BLUE, 0);  
  digitalWrite(RGB_RED, 0);
  
  int i = 0;
  float media = 0;
  delay(1000);
  while (i < 5){
    digitalWrite(RGB_RED, 1);
    digitalWrite(RGB_GREEN, 1);
    delay(500);
    digitalWrite(RGB_RED, 0);
    digitalWrite(RGB_GREEN, 0);
    lcd.clear();
    lcd.print("Aguarde...");
    musicaMedir();
    // read the input on analog pin 0:
    int sensorValue = analogRead(A0);
    // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
    float voltage = sensorValue * (5.0 / 1023.0);
    media = media + voltage;
    Serial.println(voltage);
    delay(500);
    i++;
    
  }
  // calcula media da tensao
  lcd.clear();
  lcd.print("Tensao: " + String(media/5));
  Serial.println(media/5);
  musicaFim();
  delay(5000);

  digitalWrite(RGB_GREEN, 1);  
  digitalWrite(RGB_BLUE, 0);  
  digitalWrite(RGB_RED, 0);
}


// the loop routine runs over and over again forever:
void loop() {
  
  delay(500);
  lcd.setBacklight(255);
  lcd.home();
  lcd.clear();
  lcd.print("Insira o dedo");
  delay(1000);

  int sensorValue = analogRead(A0);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  // se dedo detectado, inicia rotina de medicao
  if(voltage < float(4.8)){
    medicao();
  }


}
