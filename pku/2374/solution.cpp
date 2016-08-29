#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <algorithm>
#include <stdexcept>

#define DEBUG

long labs(long g) { return g > 0 ? g : -g; }
int min(int a, int b) { return a > b ? b : a; }
int max(int a, int b) { return a > b ? a : b; }
long lmin(long a, long b) { return a > b ? b : a; }
void dm(const char *s) { printf("%s", s); }

const int MAXN = 100001, SCALE = 100100, LEFT = 0, RIGHT = 1;
int n, s, idx[MAXN][2], next[MAXN][2];
long int opt[MAXN][2];

class Node {
  private:
    Node *_lchild, *_rchild;
    int _lbound, _rbound, _lazy_val, _val;
    bool _lazy;

    void _touch(); // pass down lazy
    void _sync();

  public:
    Node(int, int);
    Node* lchild();
    Node* rchild();
    bool isAtom();
    int mid();
    int getVal();
    void setLazy(int);
    void insert(int, int, int);
    int query(int, int);
};

Node::Node(int lbound, int rbound) : _lbound(lbound), _rbound(rbound), _lchild(NULL),
    _rchild(NULL), _lazy(false), _val(INT_MIN) {}

Node* Node::lchild() {
  if (!isAtom() && !_lchild) {
    _lchild = new Node(_lbound, mid());
  }
  return _lchild;
}

Node* Node::rchild() {
  if (!isAtom() && !_rchild) {
    _rchild = new Node(mid(), _rbound);
  }
  return _rchild;
}

int Node::getVal() {
  _touch();
  return _val;
}

bool Node::isAtom() {
  return _rbound == _lbound + 1;
}

int Node::mid() {
  return (_lbound + _rbound) >> 1;
}

void Node::insert(int i_lbound, int i_rbound, int val) {
  _touch();
  if (i_lbound == _lbound && i_rbound == _rbound) {
    setLazy(val);
    return;
  }

  if (i_lbound >= mid()) {
    rchild()->insert(i_lbound, i_rbound, val);
  }
  else if (i_rbound <= mid()) {
    lchild()->insert(i_lbound, i_rbound, val);
  }
  else {
    lchild()->insert(i_lbound, mid(), val);
    rchild()->insert(mid(), i_rbound, val);
  }

  _sync();
}

int Node::query(int q_lbound, int q_rbound) {
  _touch();
  if (q_lbound == _lbound && q_rbound == _rbound) {
    return _val;
  }
  if (q_lbound >= mid()) {
    return rchild()->query(q_lbound, q_rbound);
  }
  else if (q_rbound <= mid()) {
    return lchild()->query(q_lbound, q_rbound);
  }
  else {
    return max(
      lchild()->query(q_lbound, mid()),
      rchild()->query(mid(), q_rbound)
    );
  }
}

void Node::_sync() {
  _touch();
  if (!isAtom()) {
    _val = max(lchild()->getVal(), rchild()->getVal());
  }
}

void Node::setLazy(int lazy_val) {
  _touch();
  _lazy = true;
  _lazy_val = lazy_val;
}

void Node::_touch() {
  if (_lazy) {
    _lazy = false;
    _val = max(_val, _lazy_val);
    if (!isAtom()) {
      lchild()->setLazy(_lazy_val);
      rchild()->setLazy(_lazy_val);
    }
  }
}

void buildNext(Node *root) {
  for (int i = 1; i <= n; i ++) {
    next[i][LEFT] = max(root->query(idx[i][LEFT], idx[i][LEFT] + 1), 0);
    next[i][RIGHT] = max(root->query(idx[i][RIGHT], idx[i][RIGHT] + 1), 0);
    root->insert(idx[i][LEFT], idx[i][RIGHT] + 1, i);
  }
}

void solve() {
  Node *root = new Node(-SCALE, SCALE);
  buildNext(root);

  opt[n][LEFT] = s - idx[n][LEFT];
  opt[n][RIGHT] = idx[n][RIGHT] - s;

  long answer = LONG_MAX;

  for (int i = n; i > 0; i --) {
    for (int side = 0; side <= 1; side ++) {
      int next_seg = next[i][side];
      if (next_seg > 0) {
        opt[next_seg][LEFT] = lmin(
            opt[next_seg][LEFT],
            opt[i][side] + labs(idx[i][side] - idx[next_seg][LEFT]));
        opt[next_seg][RIGHT] = lmin(
            opt[next_seg][RIGHT],
            opt[i][side] + labs(idx[i][side] - idx[next_seg][RIGHT]));
      }
      else if (next_seg == 0) {
        answer = lmin(answer, opt[i][side] + labs(idx[i][side]));
      }
      else {
        throw std::logic_error("next_seg should not be < 0");
      }
    }
  }

  printf("%ld\n", answer);
}

inline int readInt() {
  char c = getchar();
  int mul = 1;
  while (!(c >= '0' && c <= '9')) {
    if (c == '-') {
      mul = -1;
    }
    c = getchar();
  }
  int result = 0;
  while (c >= '0' && c <= '9') {
    result = result * 10 + (c - '0');
    c = getchar();
  }
  return result * mul;
}

int main() {
  scanf("%d%d", &n, &s);
  for (int i = 1; i <= n; i ++) {
    idx[i][0] = readInt();
    idx[i][1] = readInt();
    opt[i][0] = opt[i][1] = LONG_MAX / 2;
  }
  solve();
  return 0;
}
