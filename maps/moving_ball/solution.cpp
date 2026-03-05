#include <iostream>
#include <vector>

int main() {
  int n, m;
  std::cin >> n >> m;

  std::vector<std::vector<char>> M(n, std::vector<char>(m));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      std::cin >> M[i][j];
    }
  }

  int res = 0;

  // NOTE: check the rows that they do not go up/down
  for (int i = 0; i < m; i++) {
    char top = M[0][i];
    char bot = M[n - 1][i];
    if (top == 'U')
      res++;
    if (bot == 'D')
      res++;
  }

  // NOTE: check the LHS/RHS cols so that they do not go L, R
  for (int i = 0; i < n; i++) {
    char left = M[i][0];
    char right = M[i][m - 1];
    if (left == 'L')
      res++;
    if (right == 'R')
      res++;
  }

  std::cout << res;

  return 0;
}
