#include <stdlib.h>
#include <time.h>

int main() {
  srand(time(NULL));
  int i=0, x=0, y=0;
  int n=rand()%1000;
  if (!(n>0)) return 0;
  for(i=0; i<n; i++)
  {
    x = x-y;
    y = rand();
    if (!(y!=0)) return 0;
    x = x+y;
  }
}

