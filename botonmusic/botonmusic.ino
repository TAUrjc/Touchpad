

int pinBoton2 = 2;
int pinBoton3 = 3;
int pinBoton4 = 4;
int pinLed11 = 11;
int pinLed12 = 12;
int pinLed13 =  13;   
int estadoBoton2Actual = 0;
int estadoBoton2Anterior = 0;
int estadoBoton3Actual = 0;
int estadoBoton3Anterior = 0;
int estadoBoton4Actual = 0;
int estadoBoton4Anterior = 0;
 
void setup() {
Serial.begin(9600);
// Inicializa el pin del LED como salida:
pinMode(pinLed13, OUTPUT);
pinMode(pinLed12, OUTPUT);
pinMode(pinLed11, OUTPUT);
// Inicializa el pin del botón como entrada:
pinMode(pinBoton2, INPUT);
pinMode(pinBoton3, INPUT);
pinMode(pinBoton4, INPUT);
}
 
void loop(){
  estadoBoton2Actual = digitalRead(pinBoton2);
  estadoBoton3Actual = digitalRead(pinBoton3);
  estadoBoton4Actual = digitalRead(pinBoton4);
   
  if (estadoBoton2Actual == HIGH & estadoBoton2Anterior == LOW) {
       Serial.println("2");
      digitalWrite(pinLed13, HIGH);
      estadoBoton2Anterior = estadoBoton2Actual;
  }
  
  if(estadoBoton2Actual == LOW){
      digitalWrite(pinLed13, LOW);
      estadoBoton2Anterior = estadoBoton2Actual;
  }
  
  if (estadoBoton3Actual == HIGH & estadoBoton3Anterior == LOW) {
      Serial.println("3");
      digitalWrite(pinLed12, HIGH);
      estadoBoton3Anterior = estadoBoton3Actual;
  }
  
  if(estadoBoton3Actual == LOW){
      digitalWrite(pinLed12, LOW);
      estadoBoton3Anterior = estadoBoton3Actual;
  }
  
  if (estadoBoton4Actual == HIGH & estadoBoton4Anterior == LOW) {
      Serial.println("4");
      digitalWrite(pinLed11, HIGH);
      estadoBoton4Anterior = estadoBoton4Actual;
  }
  
  if(estadoBoton4Actual == LOW){
      digitalWrite(pinLed11, LOW);
      estadoBoton4Anterior = estadoBoton4Actual;
  }
}
