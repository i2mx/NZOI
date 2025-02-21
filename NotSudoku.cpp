#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int R, C;
  cin >> R >> C;
  vector<vector<int>> grid(R, vector<int>(C));

  int bad_row, bad_col;
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      string x;
      cin >> x;
      if (x == "x") {
        bad_row = i;
        bad_col = j;
      } else {
        grid[i][j] = stoi(x);
      }
    }
  }

  int total = 0;
  for (int i = 0; i < R; i++) {
    total += grid[i][bad_col];
  }

  grid[bad_row][bad_col] = (R * (R + 1)) / 2 - total;

  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      cout << grid[i][j] << " ";
    }
    cout << endl;
  }
  return 0;
}