// https://szkopul.edu.pl/problemset/problem/klvaggzD-q4Acz_WLtkn0JXJ/site/?key=statement

#include <bits/stdc++.h>

#define endl '\n'
using namespace std;

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  // handel inputs
  int n, k;
  cin >> n;
  int b[n], c[n];
  for (int i = 0; i < n; i++)
    cin >> b[i];
  for (int i = 0; i < n; i++)
    cin >> c[i];
  cin >> k;

  // setup tables
  int distance_table[n + 1][k + 1];
  int jump_table[n + 1][k + 1];
  for (int i = 0; i <= n; i++) {
    for (int j = 0; j <= k; j++) {
      distance_table[i][j] = INT_MAX;
      jump_table[i][j] = 0;
    }
  }
  distance_table[0][0] = 0;
  jump_table[0][0] = 1;

  int best_distance_so_far =
      INT_MAX;  // if a distance every gets greater than the best distance so
                // far there is no point checking at all

  // going through the rows of the table (200)
  for (int i = 0; i < n; i++) {
    int br = b[n - 1 - i];
    int cr = c[n - 1 - i];
    // going through each cell of the row that can be reached (20_000)
    for (int current = 0; current <= k; current++) {
      if (!jump_table[i][current]) {
        continue;
      }

      int p_distance = distance_table[i][current];

      // jumping
      for (int add = 0; add <= cr; add++) {
        if (current + add * br > k) {
          break;
        }

        if (p_distance + add >= best_distance_so_far && current != k) {
          break;
        }

        if (distance_table[i + 1][current + add * br] > p_distance + add) {
          distance_table[i + 1][current + add * br] = p_distance + add;
          jump_table[i + 1][current + add * br] = add + 1;
          // update the best_distance_so_far
          if (current + add * br == k) {
            best_distance_so_far = p_distance + add;
          }
        }
      }
    }
  }

  cout << distance_table[n][k] << endl;
  int row = n;
  int col = k;
  int add, bi;

  while (row) {
    add = jump_table[row][col] - 1;
    bi = b[n - row];
    cout << add << " ";
    col -= add * bi;
    row -= 1;
  }
}