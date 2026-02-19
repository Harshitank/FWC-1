#include <Arduino.h>

int A = 10;
int B = 11;
int OUT = 9;

void setup()
{
  pinMode(A, INPUT_PULLUP);
  pinMode(B, INPUT_PULLUP);
  pinMode(OUT, OUTPUT);
}

void loop()
{
  int a = digitalRead(A);
  int b = digitalRead(B);

  int Q = a && (!b);   // Q = A B'

  digitalWrite(OUT, Q);

  delay(100);
}

