#include <bits/stdc++.h>
using namespace std;

int main() {
  long long h, w;
  cin >> h >> w;
  if (h == 1 || w == 1) {
    cout << 1 << endl;
  } else {
    cout << (h * w + 1) / 2 << endl;
    // NOTE: You if even then can divide, else odd must add one
  }
  return 0;
}
