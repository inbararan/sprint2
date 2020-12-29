                 //   W  B  R   Y   G
//const int PINS[] = {8, 9, 10, 11, 12};
                  // R   G  B   Y  W
const int PINS[] = {10, 12, 9, 11, 8};
const int HIGHS[] = {255, 255, 255, 255, 140};

void setup() {
  // Setup the laser pins as output pins
  int i;
  for (i = 0; i < 5; i++) {
    pinMode(PINS[i], OUTPUT);
  }
  // Setup serial
  Serial.begin(9600);
}



int colorIndex = 0;


int leds(int value) {
  analogWrite(PINS[colorIndex], value);
  //analogWrite(PINS[colorIndex * 2], value);
  //analogWrite(PINS[colorIndex * 2 + 1], value);
}

void loop() {
  int data_from_py;
  
  if(Serial.available() <= 0) return;
  
  data_from_py = Serial.read();

  if(data_from_py == '1')
  {
    leds(HIGHS[colorIndex]);

    colorIndex++;
    if (colorIndex == 5) {
      colorIndex = 0;
    }
  }
  else if(data_from_py =='0')
  {
    leds(0);
    
    colorIndex++;
    if (colorIndex == 5) {
      colorIndex = 0;
    }
  }
}
