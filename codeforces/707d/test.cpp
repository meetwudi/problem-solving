#include <iostream>

using namespace std;

class A {
  public:
    A() { cout << "A init" << endl; }
    void say() { cout << "say" << endl; }
};

int main() {
  A * aArr = new A [3];
  aArr[0].say();
  return 0;
}
