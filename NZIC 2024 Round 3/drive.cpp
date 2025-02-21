#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

const int B = 1474560;

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int disks = 0;

  int N, M;
  cin >> N >> M;

  for (int i = 0; i < N; i++) {
    char command;
    cin >> command;
    if (command == 'C') {  // create new file
        int y;
        cin >> y;
        int new_disks = (y + B - 1) / B;
        cout << disks + 1 << endl;
        disks += new_disks;
    }
    if (command == 'D') {  // delete file
        int x;
        cin >> x;
    }
    if (command == 'M') {  // modify file
        int x,y;
        cin >> x >> y;
    }
    if (command == 'O') { // optimize disk layout
        cout << 0 << endl;
    }
  }

  return 0;
}