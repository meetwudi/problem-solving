#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <algorithm>

using namespace std;

int myabs(int g) {
  return g >= 0 ? g : -g;
}

int compare (const void * a, const void * b)
{
    return ( *(int*)a - *(int*)b );
}

int main() {
  int n, a;
  scanf("%d%d", &n, &a);
  int * nums = new int [n];
  for (int i = 0; i < n; i ++) {
    scanf("%d", nums + i);
  }
  qsort(nums, n, sizeof *nums, compare);

  int max_num, min_num, surmax_num, surmin_num;
  if (n == 1) {
    max_num = min_num = surmin_num = surmin_num = nums[0];
  }
  else {
    max_num = nums[n - 1];
    surmax_num = nums[n - 2];
    min_num = nums[0];
    surmin_num = nums[1];
  }

  int ans;
  if (n == 1) {
    ans = 0;
  }
  else if (n == 2) {
    ans = min(myabs(a - max_num), myabs(a - min_num));
  }
  else {
    // n > 2
    ans = INT_MAX;
    // remove max_num
    if ((surmax_num > a && min_num < a) || (min_num > a && surmax_num < a)) {
      ans = min(ans, 2 * myabs(surmax_num - a) + myabs(min_num - a));
      ans = min(ans, 2 * myabs(min_num - a) + myabs(surmax_num - a));
    }
    else {
      ans = min(ans, max(myabs(min_num - a), myabs(surmax_num - a)));
    }

    // remove min_num
    if ((surmin_num > a && max_num < a) || (max_num > a && surmin_num < a)) {
      ans = min(ans, 2 * myabs(surmin_num - a) + myabs(max_num - a));
      ans = min(ans, 2 * myabs(max_num - a) + myabs(surmin_num - a));
    }
    else {
      ans = min(ans, max(myabs(max_num - a), myabs(surmin_num - a)));
    }
  }
  printf("%d\n", ans);
  return 0;
}
