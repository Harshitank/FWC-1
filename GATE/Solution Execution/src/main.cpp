#include <Arduino.h>

int X = 10;
int Y = 11;
int A = 9;

int NAND(int p, int q)
{
  return !(p && q);
}

void setup()
{
  pinMode(X, INPUT_PULLUP);
  pinMode(Y, INPUT_PULLUP);
  pinMode(A, OUTPUT);
}

void loop()
{
  int x = digitalRead(X);
  int y = digitalRead(Y);

  int P = NAND(x, y);
  int Q = NAND(x, P);
  int R = NAND(y, P);
  int Z = NAND(Q, R);

  digitalWrite(A, Z);
  delay(100);
}
