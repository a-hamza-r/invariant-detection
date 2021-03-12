/* Example from "Numerical Abstract Domains for Digital Filters"  by Feret,
   published in NSAD 05.

   First order, high bandpass filter.
*/
#include <stdlib.h>
#include <time.h>

int main()
{
  double E0, E1, S;
  int i;

  E1 = 0;
  S = 0;

  srand(time(NULL));

  for (i = 0; i <= 1000000; i++) {

    E0 = rand()%1000;

    if (rand()%2) {
      S = 0;
    }
    else {
      S = 0.999 * S + E0 - E1;
    }
    E1 = E0;

  }
  return 0;
}

