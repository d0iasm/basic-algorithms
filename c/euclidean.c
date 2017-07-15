#include <stdio.h>

int euclidean(int a, int b){
  int r = a % b;
  printf("(a, b) = (%d, %d)\n", a, b);
  if(r == 0){
    return b;
  }else{
    return euclidean(b, r);
  }
}

int main(void){
  int a = 360;
  int b = 25;
  printf("a=%d, b=%d の最大公約数は %d\n", a, b, euclidean(a, b));
  return 0;
}
