#include <stdio.h>

int h29(void){
  int a = 0xf0f0;
  int b = 0x9876;
  char s[] = "Nagoya_Univ";
  printf("%d\n%x\n%d\n%x\n%c\n", a, a<<2, a|b, a^b, s[7]);
  /* 61680 3c3c0 63734 6886 U*/
  return 0;
}

int h27(void){
  int a = 0x0f0f;
  int b = 0x1234;
  char s[] = "abcd";
  printf("%d %x %x %x %c \n", a, a<<3, a|b, a^b, s[1]);
  /* 3855 7878 1f3f 1d3b b */
  return 0;
}

int main(void){
  h29();
  h27();
  return 0;
}
