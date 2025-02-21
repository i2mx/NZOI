// I'm genuinely upset, because why does the python one MLE but this one doesn't
// are u serious right now...

// ok anyways i was not very careful of my x and y dimensions which was really 
// suboptimal but I got it figured out now!!!

#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int N, M, T;
  cin >> N >> M >> T;

  int count = 0;

  vector<vector<char>> grid(M, vector<char>(N));
  for (int i = 0; i < M; i++) {
    for (int j = 0; j < N; j++) {
      cin >> grid[i][j];
    }
  }

  queue<pair<int, int>> q;
  auto visited = vector<vector<bool>>(M, vector<bool>(N, false));
  for (int i = 0; i < M; i++) {
    for (int j = 0; j < N; j++) {
      if (visited[i][j] || grid[i][j] == '.') {
        continue;
      }
      // cout << "NEW ISLAND" << endl;
      q.push({i, j});
      visited[i][j] = true;
      int size = 0;
      while (!q.empty()) {
        auto [x, y] = q.front();
        // cout << x << " " << y << endl;
        q.pop();
        size++;
        if (x + 1 < M && grid[x + 1][y] == '#' && !visited[x + 1][y]) {
          q.push({x + 1, y});
          visited[x + 1][y] = true;
        }
        if (x - 1 >= 0 && grid[x - 1][y] == '#' && !visited[x - 1][y]) {
          q.push({x - 1, y});
          visited[x - 1][y] = true;
        }
        if (y + 1 < N && grid[x][y + 1] == '#' && !visited[x][y + 1]) {
          q.push({x, y + 1});
          visited[x][y + 1] = true;
        }
        if (y - 1 >= 0 && grid[x][y - 1] == '#' && !visited[x][y - 1]) {
          q.push({x, y - 1});
          visited[x][y - 1] = true;
        }
      }
      if (size >= T) {
        count++;
      }
    }
  }

  cout << count;
  return 0;
}