#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  char board[10][10];
  map<char, int> ships;

  for (int x = 0; x < 10; x++) {
    for (int y = 0; y < 10; y++) {
      cin >> board[x][y];
      if (ships.count(board[x][y])) {
        ships[board[x][y]] += 1;
      } else {
        ships[board[x][y]] = 1;
      }
    }
  }

  for (;;) {
    int x, y;
    cin >> x >> y;

    if (x == -1) {
      break;
    }

    char target = board[y][x];
    if (target == '#') {
      cout << "Miss" << endl;
    } else {
      ships[target] -= 1;
      if (ships[target]) {
        cout << "Hit " << target << endl;
      } else {
        cout << "Sunk " << target << endl;
      }
    }
  }

  return 0;
}