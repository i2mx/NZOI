#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int N;  // this is no more than 1000
  cin >> N;

  int total = 0;
  for (int i = 0; i < N; i++) {
    int p, d;
    cin >> p >> d;
    total += max<int>(0, p - d);
  }

  cout << total;

  return 0;
}