#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int N, M, K;
  cin >> N >> M >> K;
  string S, E;
  cin >> S >> E;
  int start, end;
  string word_list[M];
  for (size_t i = 0; i < M; i++) {
    cin >> word_list[i];
    if (word_list[i] == S)
      start = i;
    if (word_list[i] == E)
      end = i;
  }

  int best = 101;

  int cgraph[M][M];
  int dgraph[M][M];
  for (size_t i = 0; i < M; i++)
    for (size_t j = 0; j < M; j++)
      if (i == j) {
        cgraph[i][j] = 101;
        dgraph[i][j] = 101;
      } else {
        int diff = 0;
        for (size_t k = 0; k < N; k++)
          if (word_list[i][k] != word_list[j][k])
            diff++;
        cgraph[i][j] = diff - 1;
        dgraph[i][j] = diff;
      }
  
    // (distance, cost, node)
  priority_queue<pair<pair<int, int>, int>, vector<pair<pair<int, int>, int>>,
                 greater<pair<pair<int, int>, int>>>
      pq;
  pq.push({{0, 0}, start});
  while (!pq.empty()) {
    auto current = pq.top();
    int d = current.first.first;
    int c = current.first.second;
    int node = current.second;

    if (d > best)
      continue;

    // cout << d << " " << c << " " << node << endl;

    pq.pop();

    if (node == end) {
      cout << d << endl;
      return 0;
    }
    for (size_t i = 0; i < M; i++) {
      if (cgraph[node][i] + c <= K) {
        if (i == end) {
          best = min(best, d + dgraph[node][i]);
        }
        if (d+dgraph[node][i] > best) {
          continue; 
        }
        pq.push({{d + dgraph[node][i], c + cgraph[node][i]}, i});
      }
    }
  }

  cout << "IMPOSSIBLE" << endl;
  return 0;
}