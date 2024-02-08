#include <bits/stdc++.h>
using namespace std;

signed main() {
    iostream::sync_with_stdio(0);
    cin.tie(0);

    while (true)
    {
        int N;
        cin >> N;
        if (!N) return 0;

        vector<set<int>> graph(N, set<int>());
        vector<int> coloring(N, 0);
        coloring[0] = 1;

        int E;
        cin >> E;
        for (size_t i = 0; i < E; i++)
        {
            int a;
            int b;
            cin >> a >> b;
            graph[a].insert(b);
            graph[b].insert(a);
        }
        
        queue<int> q;
        q.push(0);

        while (!q.empty()){
            int current = q.front();
            q.pop();

            for(auto child: graph[current]) {
                if (coloring[child] == 0) {
                    coloring[child] = (coloring[current] + 1) % 2;
                    q.push(child);
                }
                else if(coloring[child] == coloring[current]) {
                    cout << "NOT BICOLORABLE." << '\n';
                    goto leave;
                }
            }
        } 
        cout << "BICOLORABLE." << '\n';
        leave:
        1+1;
    }
}