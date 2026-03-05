#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>

int main() {

  int n, m, k;
  std::cin >> n >> m >> k;

  std::vector<int> arr(m);
  for (int i = 0; i < m; i++) {
    std::cin >> arr[i];
  }

  // NOTE: k, m <= n | 1 <= n, m, k <= 10^5 | 1 <= ni < < n
  std::vector<int> places(n, 0);

  for (int i = 0; i < m; i++) {
    int idx = arr[i] - 1;
    if (idx - 1 >= 0 && idx - 1 < n)
      places[idx - 1]++;
    if (idx + 1 >= 0 && idx + 1 < n)
      places[idx + 1]++;
  }

  std::sort(places.begin(), places.end(), std::greater<int>());

  int res = 0;
  int limit = std::min(k, n);
  for (int i = 0; i < limit; i++) {
    res = res + places[i];
  }

  std::cout << res;

  return 0;
}
