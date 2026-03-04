#include <iostream>
#include <set>
using namespace std;

int main() {

  set<string> cards;

  std::string io;
  while (getline(cin, io)) {
    cards.insert(io);
  };

  if (cards.size() == 52) {
    cout << "YES";
  } else {
    cout << "NO";
  }

  return 0;
}
