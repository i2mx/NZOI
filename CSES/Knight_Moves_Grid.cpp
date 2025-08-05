#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<vector<int>> grid(n, vector<int>(n, 0));
    vector<vector<bool>> seen(n, vector<bool>(n, false));

    grid[0][0] = 0;
    seen[0][0] = true;

    queue<pair<int, int>> q;
    q.push({ 0,0 });

    vector<pair<int, int>> moves = { {1, 2}, {2, 1}, {-1, 2}, {-2, 1},
             {1, -2}, {2, -1}, {-1, -2}, {-2, -1} };

    while (!q.empty()) {
        auto [y, x] = q.front();
        q.pop();
        for (auto [a, b] : moves) {
            if (0 > y + a or y + a >= n) continue;
            if (0 > x + b or x + b >= n) continue;
            if (seen[y + a][x + b]) continue;
            seen[y + a][x + b] = true;
            grid[y + a][x + b] = grid[y][x] + 1;
            q.push({ y + a, x + b });
        }
    }

    for (auto row : grid) {
        for (auto elem : row) {
            cout << elem << " ";
        }
        cout << endl;
    }

    return 0;
}