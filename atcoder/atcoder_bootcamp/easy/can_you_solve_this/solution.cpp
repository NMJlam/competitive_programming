#include <ios>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int N, M, K;
  cin >> N >> M >> K;

  vector<int> B(M);
  for (int i = 0; i < M; i++) {
    cin >> B[i];
  }

  vector<vector<int>> A(N, std::vector<int>(M));
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      cin >> A[i][j];
    }
  }

  int res = 0;

  for (int i = 0; i < N; i++) {
    int solve = 0;
    for (int j = 0; j < M; j++) {
      solve = solve + A[i][j] * B[j];
    }
    if (solve + K > 0) {
      res = res + 1;
    }
  }
  cout << res;
  return 0;
}
