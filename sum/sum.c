#include <stdlib.h>
#include <time.h>

void dummyThree(int a, int n, int sn) {}
void dummyOne(int a) {}

#define a (2)
int main() { 
	dummyOne(a);
	srand(time(NULL));
  int i, n=rand()%1000, sn=0;
  dummyThree(a, n, sn);
  for(i=1; i<=n; i++) {
  dummyThree(a, n, sn);
    if (i<10) {
    sn = sn + a;
  dummyThree(a, n, sn);
    }
  dummyThree(a, n, sn);
  }
}
