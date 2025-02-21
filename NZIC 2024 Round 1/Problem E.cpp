#include <bits/stdc++.h>
#define int long long

using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    int tastiness[N];
    list<int> graph[N];

    for (size_t i = 0; i < N; i++)
        cin >> tastiness[i];    

    for (size_t i = 0; i < N; i++){
        int a,b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    bool added[N] = {0};
    added[0] = true;

    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({tastiness[0], 0});

    while (!pq.empty())
    {
        pair<int,int> top = pq.top();
        pq.pop();
        int taste, at;
        taste = top.first;
        at = top.second;

        if (taste >= M) {
            cout << taste;
            return 0;
        }

        for(auto child : graph[at])
        {
            if (added[child]) continue;
            added[child] = 1;
            pq.push({taste + tastiness[child], child});
        }

    }
    
    // cout << "hello world";
}

// line case