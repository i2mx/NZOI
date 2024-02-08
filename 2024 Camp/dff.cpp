#include <bits/stdc++.h>
using namespace std;

signed main() {
    int N;
    cin >> N;

    vector<set<int>> graph(N , set<int>()); 
    vector<bool> visted(N, false);

    int a;
    int b;
    while(cin >> a >> b) {
        graph[a].insert(b);
        graph[b].insert(a);
    }
    
    queue<int> unexplored;
    unexplored.push(0);

    while (!unexplored.empty()) {
        int node = unexplored.front();
        unexplored.pop();

        if (visted[node]) continue;

        cout << node << '\n';

        visted[node] = true;

        for (auto child : graph[node]) {
            if (!visted[child]) {
                unexplored.push(child);
            }
        }  
    }

    return 0;
}