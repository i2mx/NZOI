#include <bits/stdc++.h>
using namespace std;

signed main() {
    iostream::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    cin.ignore();

    vector<string> tasks;
    vector<int> dependencies (N, 0);

    for (size_t i = 1; i < N+1; i++) {
        string s; 
        getline(cin, s);
        tasks.push_back(s);
    }

    vector<set<int>> graph (N, set<int>());

    int a; 
    int b;

    while(cin >> a >> b) {
        graph[a].insert(b);
        dependencies[b] += 1;
    }

    queue<int> q;

    for (size_t i = 0; i < N; i++)
    {
        if (dependencies[i] == 0) {
            q.push(i);
        }
    }

    while(!q.empty()) {
        int top = q.front();
        q.pop();

        cout << tasks[top] << '\n';

        for (int next : graph[top]) {
            dependencies[next] -= 1;
            if (dependencies[next] == 0) {
                q.push(next);
            }
        }

    }
    



    return 0;
}