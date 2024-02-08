#include <bits/stdc++.h>

using namespace std;

signed main() {
    int N;
    cin >> N;

    int E;
    cin >> E;

    int T;
    cin >> T;

    vector<set<pair<int,int>>> graph(N+1, set<pair<int,int>>()); 
    vector<int> distances(N+1, INT_MAX);
    distances[E] = 0;

    int a;
    int b;
    int c;

    int M;
    cin >> M;

    for(int i = 0; i < M; i++) {
        cin >> a >> b >> c;
        graph[b].insert(make_pair(c, a));
    }
    
    // weight and node number
    priority_queue<pair<int ,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push(make_pair(0, E));

    while(!pq.empty()) {
        int distance = pq.top().first;
        int parent = pq.top().second;

        // cout << parent << endl;
        pq.pop();

        if (distance > distances[parent]) {
            continue;
        }

        if (distance > T) {
            continue;
        }

        for (pair<int,int> p : graph[parent]) {
            int child = p.second;
            int child_distance = p.first + distance;

            if (child_distance >= distances[child]) {
                continue;
            }

            if (child_distance > T) {
                continue;
            }

            distances[child] = child_distance;

            pq.push(make_pair(child_distance, child));
        }
    }
    

    int count = 0;
    for (int p : distances) {
        if ( p <= T ){
            count += 1;
        }
    }
    
    cout << count;

    return 0;
}