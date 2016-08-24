#include <cstdio>
#include <cstring>
#include <bitset>

using namespace std;

const int MAXQ = 100000;
const int BITSIZE = 1001;
bitset<BITSIZE> shelves[MAXQ + 1];
bitset<BITSIZE> mask;

int main() {
  int n, m, q;
  scanf("%d%d%d", &n, &m, &q);
  shelves[0].reset();

  mask.reset();
  for (int i = 0; i < m; i ++) {
    mask.set(i);
  }

  int ** history = new int * [q + 1];
  int * sum = new int [q + 1];
  history[0] = new int [n];
  memset(history[0], 0, sizeof(history[0][0]) * n);
  sum[0] = 0;

  for (int qry = 1; qry <= q; qry ++) {
    history[qry] = new int [n];

    int op, args[2];
    scanf("%d", &op);
    if (op == 1 || op == 2) {
      scanf("%d%d", args, args + 1);
      args[0] -= 1;
      args[1] -= 1;
    }
    else if (op == 3) {
      scanf("%d", args);
      args[0] -= 1;
    }
    else {
      // op == 4
      scanf("%d", args);
    }

    if (op != 4) {
      memcpy(history[qry], history[qry - 1], sizeof(history[qry - 1][0]) * n);
    }
    else {
      memcpy(history[qry], history[args[0]], sizeof(history[args[0]][0]) * n);
      sum[qry] = sum[args[0]];
    }

    if (op == 1) {
      sum[qry] = sum[qry - 1];
      shelves[qry] = shelves[history[qry][args[0]]];
      history[qry][args[0]] = qry;
      if (shelves[qry][args[1]] == 0) {
        shelves[qry][args[1]] = 1;
        sum[qry] += 1;
      }
    }
    if (op == 2) {
      sum[qry] = sum[qry - 1];
      shelves[qry] = shelves[history[qry][args[0]]];
      history[qry][args[0]] = qry;
      if (shelves[qry][args[1]] == 1) {
        shelves[qry][args[1]] = 0;
        sum[qry] -= 1;
      }
    }
    if (op == 3) {
      sum[qry] = sum[qry - 1];
      shelves[qry] = shelves[history[qry][args[0]]];
      history[qry][args[0]] = qry;
      sum[qry] -= shelves[qry].count();
      shelves[qry] = (~shelves[qry]) & mask;
      sum[qry] += shelves[qry].count();
    }
    printf("%d\n", sum[qry]);
  }

  for (int i = 0; i < q + 1; i ++) {
    delete[] history[i];
  }
  delete[] history;
  return 0;
}
