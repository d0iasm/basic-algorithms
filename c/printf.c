#include <stdio.h>

int h29(void){
  int a=0xf0f0;
  int b=0x9876;
  char s[]="Nagoya_Univ";
  printf("%d\n%x\n%d\n%x\n%c\n", a, a<<2, a|b, a^b, s[7]);
  return 0;
}

int main(void){
  h29();
  return 0;
}
