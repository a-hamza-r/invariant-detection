#include <stdlib.h>
#include <time.h>

#define a (2)
int main() { 
  srand(time(NULL));
  int i, n=rand()%1000, sn=0;
  for(i=1; i<=n; i++) {
    if (i<10)
    sn = sn + a;
  }
}
