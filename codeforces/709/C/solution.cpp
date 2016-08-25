#include <cstdio>
#include <cstring>

int main() {
  char * c = new char [1000001];
  scanf("%s", c);
  int n = strlen(c), first_a = 0;
  while (first_a < n && c[first_a] == 'a') first_a ++;
  if (first_a == n) {
    // all 'a'
    c[n - 1] = 'z';
    printf("%s", c);
    return 0;
  }
  int next_a = first_a + 1;
  while (next_a < n && c[next_a] != 'a') next_a ++;
  for (int i = first_a; i < next_a; i ++) {
    c[i] --;
  }
  printf("%s", c);
  return 0;
}
