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

    int N, M, G; cin >> N >> M >> G;
    vector<vector<pair<int, int>>> graph(N);
    for (int i = 0; i < M; i++) {
        int a, b, c; cin >> a >> b >> c;
        graph[a].push_back({ c,b });
        graph[b].push_back({ c,a });
    }

    // djikstras to get all the annoying nodes
    vector<int> gnome_distance(N, INT_MAX);
    vector<bool> annoying(N, false);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> gq;
    for (int i = 0; i < G; i++) {
        int g, r;
        cin >> g >> r;
        gnome_distance[g] = -r;
        gq.push({ -r, g });
        annoying[g] = true;
    }

    while (!gq.empty()) {
        auto [d, u] = gq.top(); gq.pop();
        if (d < gnome_distance[u]) continue;
        for (auto [w, v] : graph[u]) {
            if (d + w < gnome_distance[v]) {
                gnome_distance[v] = d + w;
                if (d + w <= 0) {
                    annoying[v] = true;
                    gq.push({ d + w, v });
                }
            }
        }
    }
    vector<pair<int, int>> distance(N, { INT_MAX, INT_MAX });
    using P = pair<pair<long long, long long>, long long>;

    priority_queue <P, vector<P>, greater<P>> q;
    q.push({ {(int)annoying[0], 0}, 0 });
    while (!q.empty()) {
        auto [d, u] = q.top();
        auto [da, dd] = d;
        q.pop();
        if (da > distance[u].first) continue;
        if (da == distance[u].first && dd > distance[u].second) continue;

        if (u == N - 1) {
            cout << da << '\n' << dd;
            return 0;
        }

        for (auto [w, v] : graph[u]) {
            int a = annoying[v];

            if (da + a > distance[v].first) continue;
            if (da + a == distance[v].first && dd + w >= distance[v].second) continue;

            distance[v] = { da + a, dd + w };
            q.push({ {da + a, dd + w}, v });
        }

    }
    return 0;
}

// wow the debugger might actually be useful?
// oh my god i forgot that the starting node can also be annoying