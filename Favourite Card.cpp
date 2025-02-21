#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int N, S; 
  cin >> N >> S;

  int x;
  for (int i = 0; i < N; i++) {
    cin >> x;
    if(x == S) {
      cout << i;
      return 0;
    }
  }

  return 1;
}