

int pinBoton = 2;  
int pinLed =  13;   
int estadoBoton = 0;  
 
void setup() {
Serial.begin(9600);
// Inicializa el pin del LED como salida:
pinMode(pinLed, OUTPUT);
// Inicializa el pin del botón como entrada:
pinMode(pinBoton, INPUT);
}
 
void loop(){
  estadoBoton = digitalRead(pinBoton);
   
  if (estadoBoton == HIGH) {
    //if(estadoBoton == LOW){
       Serial.println("1");
      digitalWrite(pinLed, HIGH);
    //}
  } else {
     digitalWrite(pinLed, LOW);
  }
}
