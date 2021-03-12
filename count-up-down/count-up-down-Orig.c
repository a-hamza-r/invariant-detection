#include <stdlib.h>
#include <time.h>

int main()
{
  srand(time(NULL));
  int n = rand()%1000;
  int x=n, y=0;
  while(x>0)
  {
    x--;
    y++;
  }
}

