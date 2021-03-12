#include <stdlib.h>
#include <time.h>

void dummyThree(int x, int y, int n) {}
void dummyOne(int n) {}

int main()
{
	srand(time(NULL));
  int n = rand()%1000;
  dummyOne(n);
  int x=n, y=0;
  dummyThree(x, y, n);
  while(x>0)
  {
    x--;
	  dummyThree(x, y, n);
    y++;
	  dummyThree(x, y, n);
  }
}

