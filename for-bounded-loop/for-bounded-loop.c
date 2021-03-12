#include <stdlib.h>
#include <time.h>

void dummyThree(int x, int y, int n) {}
void dummyTwo(int x, int y) {}

int main() {
	srand(time(NULL));
  int i=0, x=0, y=0;
  dummyTwo(x, y);
  int n=rand()%1000;
  dummyThree(x, y, n);
  if (!(n>0)) return 0;
  dummyThree(x, y, n);
  for(i=0; i<n; i++)
  {
    x = x-y;
	  dummyThree(x, y, n);
    y = rand();
	  dummyThree(x, y, n);
    if (!(y!=0)) return 0;
	  dummyThree(x, y, n);
    x = x+y;
	  dummyThree(x, y, n);
  }
}

