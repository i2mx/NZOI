#include <bits/stdc++.h>

using namespace std;

int main() {
    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL);

    int N;
    cin >> N;

    vector<set<int>> graph (N, set<int>());
    vector<int> parent (N, -1);

    int a;
    int b;
    while (cin >> a >> b) {
        graph[a].insert(b);
        graph[b].insert(a);
    }

    queue<int> search;
    search.push(0);

    while (!search.empty()) {
        int current = search.front();
        search.pop();

        if (current == N-1) {
            break;
        }

        for(auto child : graph[current]) {
            if(parent[child] == -1) {
                parent[child] = current;
                search.push(child);
            }
        }
    }

    stack<int> path;
    int current = N - 1;

    do {
        path.push(current);
        current = parent[current];
    } while (current != 0);

    path.push(0);

    while (!path.empty()) {
        int x = path.top();
        path.pop();
        cout << x << " ";
    }

    return 0;
}