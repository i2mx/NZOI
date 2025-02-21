#include <bits/stdc++.h>

#define int long long
// #define endl '\n'
using namespace std;

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int N;
  cin >> N;

  string words[N];
  for (int i = 0; i < N; i++) {
    string word;
    getline(cin, word);
    words[N] = word;
    cout << words[N];
  }

  cout << flush;

  char c;
  cin >> c;

  for (string word : words) {
    int total = 0;
    for (char a : word) {
      if (a == c) {
        total += 1;
      }
    }
    cout << total << endl;
  }

  return 0;
}