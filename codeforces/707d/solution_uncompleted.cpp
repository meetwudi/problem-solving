#include <iostream>
#include <vector>
#include <queue>
#include <bitset>

using namespace std;

class Node {
  int version;
  int *args;

  public:
    void setVersion(int);
    void setArgs(int*);
    Node();
    queue<Node*> childs;
};

void Node::setVersion(int _version) {
  version = _version;
}

void Node::setArgs(int * _args) {
  args = _args;
}

Node::Node() : version(0), args(NULL) {}

void sink(Node * current, int * answer, bitset<1001> * shelf) {
  while (current->childs->front()) {
    Node * first_child = current->childs->pop_front();
    if (first_child.args[0] == 1 && shelf[first_child.args[1]][first_child.args[2]] == 0) {
    }
  }
}

void solve(Node * root, int * answer, int n, const int m) {
  vector<Node*> stack;
  bitset<1001> * shelf = new bitset<1001>[n];
  stack.push_back(root);
  
  
}

int main() {
  int n, m, q;
  cin >> n >> m >> q;

  int * answer = new int [q + 1];
  Node * nodes = new Node [q + 1];
  Node * root = nodes;
  Node * current = root;
  answer[0] = 0;

  for (int qry = 0; qry < n; qry ++) {
    int * args = new int [3];
    int op = args[0];
    cin >> args[0];
    if (op == 1 || op == 2) {
      cin >> args[1] >> args[2];
    }
    else {
      cin >> args[1];
    }

    nodes[qry].setVersion(qry);
    nodes[qry].setArgs(args);

    if (op != 4) {
      current->childs.push(&nodes[qry]);
    }
    else {
      nodes[args[1]].childs.push(&nodes[qry]);
    }
    current = &nodes[qry];
  }

  solve(root, answer, n, m);

  delete[] answer;
  delete[] nodes;
  return 0;
}
