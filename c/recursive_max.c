#include <stdio.h>

int recursive_max(int a[], int n){
  int v1, v2;
  if(n == 1){
    return a[0];
  }else{
    v1 = recursive_max(a, n-1);
    v2 = a[n-1];
    if(v1 > v2){
      return v1;
    }else{
      return v2;
    }
  }
}

int main(void){
  int a[] = {3, 2, 5, 0, 8};
  printf("[3, 2, 5, 0, 8] の最大値は %d\n", recursive_max(a, 5));
  return 0;
}
