

int pinBoton2 = 2;
int pinBoton3 = 3;
int pinBoton4 = 4;
int pinLed11 = 11;
int pinLed12 = 12;
int pinLed13 =  13;   
int estadoBoton2 = 0;
int estadoBoton3 = 0;  
int estadoBoton4 = 0;  
 
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
  estadoBoton2 = digitalRead(pinBoton2);
  estadoBoton3 = digitalRead(pinBoton3);
  estadoBoton4 = digitalRead(pinBoton4);
   
  if (estadoBoton2 == HIGH) {
    //if(estadoBoton == LOW){
       Serial.println("2");
      digitalWrite(pinLed13, HIGH);
    //}
  } else {
     digitalWrite(pinLed13, LOW);
  }
  
  if (estadoBoton3 == HIGH) {
    //if(estadoBoton == LOW){
       Serial.println("3");
      digitalWrite(pinLed12, HIGH);
    //}
  } else {
     digitalWrite(pinLed12, LOW);
  }
  if (estadoBoton4 == HIGH) {
    //if(estadoBoton == LOW){
       Serial.println("4");
      digitalWrite(pinLed11, HIGH);
    //}
  } else {
     digitalWrite(pinLed11, LOW);
  }
}
