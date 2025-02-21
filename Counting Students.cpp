#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int N;
  cin >> N;

  unordered_set<int> numbers;
  set<int> duplicates;
  
  for (int i = 0; i < N; i++) {
    int x;
    cin >> x;
    if(numbers.count(x) && !duplicates.count(x)){
      duplicates.insert(x);
    }
    numbers.insert(x);
  }

  for(int x : duplicates) {
    cout << x << endl;
  }

  return 0;
}