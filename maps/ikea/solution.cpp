#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;

  string table_prices;
  cin >> table_prices;

  string res;

  for (int i = 0; i < 2 * n; i = i + 2) {
    char left = table_prices[i];

    if (left == 'T') {
      res = res + 'R';
    } else {
      res = res + 'L';
    }
  }

  cout << res;

  return 0;
}
