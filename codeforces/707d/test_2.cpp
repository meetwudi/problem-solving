#include <cstdio>

int main() {
  int ** aint = new int * [4];
  for (int i = 0; i < 4; i ++) {
    aint[i] = new int [4];
  }
  printf("sizeof(aint): %ld\n", sizeof(aint));
  printf("sizeof(aint[0]): %ld\n", sizeof(aint[0]));
  return 0;
}
