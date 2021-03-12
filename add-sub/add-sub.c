/* Rounding addition and subtraction in double-precision floats. */

#include <stdlib.h>
#include <time.h>

void dummyOne(int x) {}
void dummyTwo(int x, int y) {}
void dummyThree(int x, int y, int z) {}

int main()
{
  double x, y, z, r;

  srand(time(NULL));
  x = rand();
  dummyOne(x);
  y = x + 1;
  dummyTwo(x, y);
  z = x - 1;
  dummyThree(x, y, z);
  r = y - z;  
  dummyThree(x, y, z);
  return 0;
}
