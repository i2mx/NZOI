#include <bits/stdc++.h>
using namespace std;

// #define int long long

signed main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        int M;

        cin >> N >> M;
        vector< tuple<int,int,int>> edges;
        for (size_t i = 0; i < M; i++) {
            int a, b, c;
            cin >> a >> b >> c;
            edges.push_back({a,b,c});
        }
        int dist[1010]{}, ok = 0;
        for(int i = 0; i < N; i++) {
            for(auto [u,v,w]: edges) {
                if(dist[v]>dist[u]+w) {
                    if(i==N-1)
                        ok=1;
                    else
                        dist[v]=dist[u]+w;
                }
            }   
        }
        cout << (ok?"possible\n":"not possible\n");
    }
    return 0;
}