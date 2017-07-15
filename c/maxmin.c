#include <stdio.h>

int max(int s[], int n){
  int max = s[0];
  int i;
  for(i = 0; i < n; i++){
    printf("max() の比較演算の回数は %d 回目\n", i);
    if(s[i] > max){
      max = s[i];
    }
  }
  return max;
}

int *maxmin(int s[], int n, int *list){
  if(n <= 2){
    if(s[0] > s[1]){
      list[0] = s[0];
      list[1] = s[1];
    }else{
      list[1] = s[0];
      list[0] = s[1];
    }
    return list;
  }

  int m = n/2;
  int i;
  int a[m], b[m];
  for(i=0; i<m; i++){
    a[i] = s[i];
  }
  for(i=m; i<n; i++){
    b[i] = s[i];
    printf("b[%d] = %d\n", i, b[i]);
  }
  list = maxmin(a, m, list);
  list = maxmin(b, m, list);
  /* TODO: listに正しい値が入っていない */
  
  return list;
}

int main(void){
  int s[] = {2,4,1,6,3,5,7,0};
  int list[2];
  printf("[2,4,1,6,3,5,7,0] のmax値は %d\n", max(s, 8));
  printf("[2,4,1,6,3,5,7,0] のmax値は %d, min値は %d\n", maxmin(s, 8, list)[0], maxmin(s, 8, list)[1]);
  return 0;
}
