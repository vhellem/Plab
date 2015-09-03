
const int buttonPin = 2; 
const int dotPin  = 13;
const int dashPin = 11;
const int pausePin = 9;

int countLow= 0;
int countPress = 0 ; 
boolean pres ; 
boolean checkLow  ;
boolean first = false; 
int pauses = 0 ; 

int buttonState ; 



void setup() {
  pinMode(dotPin, OUTPUT); 
  pinMode(dashPin, OUTPUT); 
  pinMode(buttonPin, INPUT); 
  Serial.begin(9600);
  
  
  digitalWrite(pausePin, OUTPUT); 
  
}

void loop() {
  buttonState = digitalRead(buttonPin); 
  
  if(buttonState == HIGH) {
    if(pauses>= 4){
      Serial.println(4);
    }
    if(pauses<= 3 && pauses>= 1){
      Serial.println(3); 
    }
    pauses = 0 ; 
    delay(100); 
    countPress += 1;
    checkLow = true; 
    countLow = 0 ; 
    first = true; 
  }
  
  else{
    if(checkLow == true){
      
      if(countPress<3) {
        digitalWrite(dotPin, HIGH); 
        Serial.println(1);
        delay(200); 
        digitalWrite(dotPin, LOW);
      }
      else{
        digitalWrite(dashPin, HIGH); 
        Serial.println(2);
        delay(200);
        digitalWrite(dashPin, LOW); 
      }
      checkLow = false;
      countPress = 0 ; 
      }
  if(first==true){
    delay(100);
    countLow += 1;
    if(countLow > 15){
      pauses += 1; 
      
      
      
  }}
}}
