#include <stdlib.h>
#include <time.h>

int main()
{
  srand(time(NULL));
  int x=rand()%100;
  int z=rand()%200;

  while(x<100 && 100<z) 
  {
    int tmp=rand()%2;
    if (tmp)
   {
     x++;
   }
   else
   {
     x--;
     z--;
   }
  }                       
    
  return 0;
}


