#include <stdlib.h>
#include <time.h>

void dummyThree(int a, int j, int sn) {}
void dummyOne(int a) {}

#define a (2)
int main() { 
	dummyOne(a);
	srand(time(NULL));
  int i, j=10, n=rand()%1000, sn=0;
  dummyThree(a, j, sn);
  for(i=1; i<=n; i++) {
    if (i<j) {
    sn = sn + a;
  dummyThree(a, j, sn);
	}
    j--;
  dummyThree(a, j, sn);
  }
}
