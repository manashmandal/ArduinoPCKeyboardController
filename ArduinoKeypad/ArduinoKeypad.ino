// Author: Manash
// Demo code for controlling pc keyboard using arduino


#include <Keypad.h>
#define BAUD 9600

const byte ROWS = 4; //four rows
const byte COLS = 4; //three columns
char keys[ROWS][COLS] = {
  {'1','2','3', 'A'},
  {'4','5','6', 'B'},
  {'7','8','9', 'C'},
  {'#','0','*', 'D'}
};
byte rowPins[ROWS] = {22, 23, 24, 25}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {26, 27, 28, 29}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

void setup(){
  Serial.begin(BAUD);
}

void loop(){
  char key = keypad.getKey();

  if (key != NO_KEY){
    if (key == '1'){
      Serial.print("tab\n");
    } else if (key == '2'){
      Serial.print("space\n");
    } else if (key == '3') {
      Serial.print("capslock\n");
    }
  }
}
