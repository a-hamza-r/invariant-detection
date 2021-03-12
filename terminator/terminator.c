#include <stdlib.h>
#include <time.h>

void dummyThree(int x, int z, int tmp) {}
void dummyOne(int x) {}
void dummyTwo(int x, int z) {}

int main()
{
	srand(time(NULL));
  int x=rand()%100;
  dummyOne(x);
  int z=rand()%200;
  dummyTwo(x, z);

  while(x<100 && 100<z) 
  {
    int tmp=rand()%2;
    dummyThree(x, z, tmp);
    if (tmp)
   {
     x++;
    dummyThree(x, z, tmp);
   }
   else
   {
     x--;
    dummyThree(x, z, tmp);
     z--;
    dummyThree(x, z, tmp);
   }
  }                       
    
  return 0;
}


