#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

template<typename T, typename S>
ostream& operator<<(ostream& os, pair<T, S> p) {
    os << "(" << p.first << ", " << p.second << ")";
    return os;
}

template <typename T>
ostream& operator<<(ostream& os, vector<T> v) {
    os << "[";
    for (int i = 0; i < v.size(); ++i) {
        os << v[i];
        if (i != v.size() - 1) {
            os << ", ";
        }
    }
    os << "]";
    return os;
}

#define all(v) begin(v), end(v)

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<vector<int>> graph(n + 1);
        for (int i = 0; i < n - 1; i++) {
            int a, b;
            cin >> a >> b;
            graph[a].push_back(b);
            graph[b].push_back(a);
        }
        vector<int> adj_leafs(n + 1, 0);
        int leaf_count = 0;
        for (int i = 1; i <= n; i++) {
            if (graph[i].size() == 1) {
                adj_leafs[i]++;
                adj_leafs[graph[i][0]]++;
                leaf_count++;
            }
        }

        cout << leaf_count - *max_element(all(adj_leafs)) << endl;
    }

    return 0;
}