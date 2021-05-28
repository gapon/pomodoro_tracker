const int redPin = 10;
const int bluePin = 11;
int message;


void setup() {
  Serial.begin(9600);
  
  pinMode(redPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

}

void loop() {
  if (Serial.available() > 0) {
    message = Serial.read();
    Serial.println(message);

    if (message == 'F') {
      digitalWrite(bluePin, HIGH);
      digitalWrite(redPin, LOW);
    }
    if (message == 'N') {
      digitalWrite(bluePin, LOW);
      digitalWrite(redPin, HIGH);
    }   
  
  }

}
