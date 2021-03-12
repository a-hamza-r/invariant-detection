/* Rounding addition and subtraction in double-precision floats. */

#include <stdlib.h>
#include <time.h>

int main()
{
  double x, y, z, r;

  srand(time(NULL));
  x = rand();
  y = x + 1;
  z = x - 1;
  r = y - z;  
  return 0;
}
