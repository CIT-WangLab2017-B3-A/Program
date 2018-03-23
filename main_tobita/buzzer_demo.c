#include <wiringPi.h>
#include <string.h>

#define PIN 20
int Do = 261;
int DoS = 277;
int Re = 293;
int Mi = 330;
int Fa = 349;
int FaS = 370;
int So = 392;
int SoS = 415;
int Ra = 440;
int Si = 494;

void tone(int freq, float time){
    int i;
    int loop = (int)(time*(float)freq);
    float fwait=((1.0/(float)freq)/2.0);
    int wait=(int)(fwait*1000000.0);
    for(i=0; i<loop; i++){
        digitalWrite(PIN, HIGH);
        delayMicroseconds(wait);
        digitalWrite(PIN, LOW);
        delayMicroseconds(wait);
    }
}

void mac(void){
    int i;
    for(i=0; i<3; i++){
        tone(2*Ra,0.3);
        tone(2*So,0.3);
        tone(2*Ra,0.3);
        delay(200);
    }
    delay(1000);
}
void tel(void){
    int i;
    for(i=0; i<3; i++){
        tone(4*Si, 0.05);
        tone(4*Do, 0.05);
        delay(10);
        tone(4*Si, 0.05);
        tone(4*Do, 0.05);
        delay(500);
    }
    delay(1000);
}
void famima(void){
    tone(2*FaS, 0.25);
    tone(2*Re,  0.25);
    tone(1*Ra,  0.25);
    tone(2*Re,  0.25);
    tone(2*Mi,  0.25);
    tone(2*Ra,  0.4);
    delay(40);
    tone(1*Ra,  0.3);
    tone(2*Mi,  0.25);
    tone(2*FaS, 0.25);
    tone(2*Mi,  0.25);
    tone(1*Ra,  0.25);
    tone(2*Re,  0.4);
}

void hoge(void){
    tone(10000,0.5);
}

int main(int argc, char *argv[]){
    if(argc <= 1) return 1;
    if(wiringPiSetupGpio() == -1) return 1;
    pinMode(PIN, OUTPUT);
    if(strcmp(argv[1], "mac")==0) mac();
    else if(strcmp(argv[1], "tel")==0) tel();
    else if(strcmp(argv[1], "famima")==0) famima();
    else if(strcmp(argv[1], "hoge")==0) hoge();

    return 0;
}
