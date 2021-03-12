/* Example from "Numerical Abstract Domains for Digital Filters"  by Feret,
   published in NSAD 05.

   First order, high bandpass filter.
*/
#include <stdlib.h>
#include <time.h>

void dummyThree(int E0, int E1, int S) {}
void dummyOne(int E1) {}
void dummyTwo(int E1, int S) {}

int main()
{
  int E0, E1, S;
  int i;

  E1 = 0;
  dummyOne(E1);
  S = 0;
  dummyTwo(E1, S);

  srand(time(NULL));

  for (i = 0; i <= 1000; i++) {

    E0 = rand()%1000;
    dummyThree(E1, S, E0);
    if (rand()%2) {
      S = 0;
	    dummyThree(E1, S, E0);
    }
    else {
      S = 0.999 * S + E0 - E1;
	    dummyThree(E1, S, E0);
    }
    E1 = E0;
    dummyThree(E1, S, E0);

  }
  return 0;
}

