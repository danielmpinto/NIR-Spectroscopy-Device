#include <Wire.h>
#include "MAX30100_PulseOximeter.h"
#include <LiquidCrystal_PCF8574.h>
 
LiquidCrystal_PCF8574 lcd(0x27);  // set the LCD address to 0x27 for a 16 chars and 2 line display


byte dotOff[] = { 0b00000, 0b01110, 0b10001, 0b10001,
                  0b10001, 0b01110, 0b00000, 0b00000 };
byte dotOn[] = { 0b00000, 0b01110, 0b11111, 0b11111,
                 0b11111, 0b01110, 0b00000, 0b00000 };

#define REPORTING_PERIOD_MS     1000

PulseOximeter pox;
uint32_t tsLastReport = 0;

// Make custom characters:
byte Heart[] = {
  B00000,
  B01010,
  B11111,
  B11111,
  B01110,
  B00100,
  B00000,
  B00000
};

void loading(){
  lcd.setBacklight(255);
  lcd.home();
  lcd.clear();
  lcd.print("Iniciando. ");
}  
 
void onBeatDetected()
{
    Serial.println("Beat!");
    lcd.setCursor(0,0);
    lcd.print("+");
}
 
void setup()
{   
    
    Serial.begin(115200);
    Serial.println("LCD...");
    
    Wire.begin();
    Wire.beginTransmission(0x27);
  
    lcd.begin(16, 2);  // initialize the lcd
  
    lcd.createChar(1, dotOff);
    lcd.createChar(2, dotOn);
    loading();


    Serial.print("Initializing pulse oximeter..");
   // set up the LCD's number of columns and rows: 
  lcd.begin(16, 2);

    // Initialize the PulseOximeter instance
    // Failures are generally due to an improper I2C wiring, missing power supply
    // or wrong target chip
    if (!pox.begin()) {
        Serial.println("FAILED");
        for(;;);
    } else {
        Serial.println("SUCCESS");
    }
     pox.setIRLedCurrent(MAX30100_LED_CURR_7_6MA);
 
    // Register a callback for the beat detection
    pox.setOnBeatDetectedCallback(onBeatDetected);
}
 
void loop()
{
    float bpm;
    float oxi;
    float glucose;
    lcd.createChar(0, Heart);
    while (true){
    // Make sure to call update as fast as possible
      pox.update();
      if (millis() - tsLastReport > REPORTING_PERIOD_MS) {
          bpm = pox.getHeartRate();
          oxi = pox.getSpO2();
          Serial.print("Heart rate:");
          Serial.print(bpm);
          Serial.print("bpm / SpO2:");
          Serial.print(oxi);
          lcd.clear();
          // bpm heart on first
          lcd.setCursor(1, 0);
          lcd.write(byte(0));
          lcd.setCursor(0, 1);
          lcd.print(bpm);
          //

          // setting up oxygen level
          lcd.setCursor(7,0);
          lcd.print("Oxy");
          lcd.setCursor(7,1);
          lcd.print(oxi);
          //

          // set glucose
          lcd.setCursor(13,0);
          lcd.print("Glu");
          lcd.setCursor(13,1);
          glucose = 16714.61 + 0.47 * bpm -351.045 * oxi + 1.85 *(oxi * oxi);
          lcd.print(int(glucose));
          //
          Serial.println("%");
          
          
   
          tsLastReport = millis();
      }
    }
}
