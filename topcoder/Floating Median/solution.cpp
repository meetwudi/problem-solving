#include <cstdio>
#include <queue>
#include <stdexcept>

//#define DEBUG
#define USE_MAIN
#ifdef DEBUG
#define dd(name, xx) printf("%s: %d\n", name, xx);
#define ds(xx) printf("%s\n", xx);
#else
#define dd(name, xx) {};
#define ds(xx) {};
#endif

class Node {
  private:
    int lbound, rbound;
    int sum;
    Node *lchild, *rchild;
  public:
    Node(int, int);
    int getMid();
    int getKthMinimum(int);
    int getSum();
    void modifySum(int, int);
    Node* getLeftChild();
    Node* getRightChild();

    static Node* buildTree(int, int);
};

Node::Node(int _lbound, int _rbound) : lbound(_lbound), rbound(_rbound) {
  sum = 0;
  lchild = rchild = NULL;
}

int Node::getMid() {
  return (lbound + rbound) >> 1;
}

Node* Node::getLeftChild() {
  if (!lchild && rbound > lbound + 1) {
    lchild = new Node(lbound, getMid());
  }
  return lchild;
}

Node* Node::getRightChild() {
  if (!rchild && rbound > lbound + 1) {
    rchild = new Node(getMid(), rbound);
  }
  return rchild;
}

int Node::getKthMinimum(int k) {
  if (k <= 0 || k > sum) {
    throw std::logic_error("[getKthMinimum] k should <= sum and >= 0");
  }
  if (rbound == lbound + 1) {
    return lbound;
  }
  if (k > lchild->getSum()) {
    return rchild->getKthMinimum(k - lchild->getSum());
  }
  else {
    return lchild->getKthMinimum(k);
  }
}

int Node::getSum() {
  return sum;
}

void Node::modifySum(int pos, int delta) {
  if (pos < lbound || pos >= rbound) {
    dd("exception pos", pos);
    throw std::logic_error("[modifySum] position out of bound");
  }
  sum += delta;
  if (rbound > lbound + 1 && pos < getMid()) {
    getLeftChild()->modifySum(pos, delta);
  }
  if (rbound > lbound + 1 && pos >= getMid()) {
    getRightChild()->modifySum(pos, delta);
  }
}

Node* Node::buildTree(int lbound, int rbound) {
  if (rbound <= lbound) {
    throw std::logic_error("[buildTree] rbound should be greater than lbound");
  }
  Node* root = new Node(lbound, rbound);

  std::queue<Node*> que;
  que.push(root);
  while (!que.empty()) {
    Node* current = que.front();
    que.pop();
    if (current->getLeftChild() != NULL) {
      que.push(current->getLeftChild());
    }
    if (current->getRightChild() != NULL) {
      que.push(current->getRightChild());
    }
  }

  return root;
}

int nextVal(int current, int mul, int add, int MOD) {
  long answer = (long)current * mul + add;
  return (int)(answer % MOD);
}

long long solve(int seed, int mul, int add, int n, int k) {
  int current_val = seed;
  long long answer = 0ll;
  const int MOD = 65536;

  Node *root = Node::buildTree(0, MOD + 1);
  std::queue<int> num_que;
  for (int i = 0; i < n; i ++) {
    if (num_que.size() == k) {
      int removal = num_que.front();
      num_que.pop();
      root->modifySum(removal, -1);
      dd("remove num", removal);
    }
    dd("add num", current_val);
    root->modifySum(current_val, 1);
    num_que.push(current_val);
    current_val = nextVal(current_val, mul, add, MOD);

    if (num_que.size() == k) {
      answer += (long long) root->getKthMinimum((k + 1) >> 1);
      dd("medium", root->getKthMinimum((k + 1) >> 1));
    }
  }
  return answer;
}

class FloatingMedian {
  public:
    long long sumOfMedians(int seed, int mul, int add, int N, int K) {
      return solve(seed, mul, add, N, K);
    }
};


#ifdef USE_MAIN
int main() {
  int seed, mul, add, n, k;
  scanf("%d%d%d%d%d", &seed, &mul, &add, &n, &k);
  printf("%lld\n", (new FloatingMedium())->sumOfMedians(seed, mul, add, n, k));
  return 0;
}
#endif




