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

    int N, S, E; cin >> N >> S >> E;
    vector<pair<int, int>> pieces(N);
    for (int i = 0; i < N; ++i) {
        int start, end;
        cin >> start >> end;
        pieces[i] = { start, end };
    }

    sort(all(pieces));

    // check that something crosses S at all
    bool valid = false;
    for (int i = 0; i < N; i++) {
        if (pieces[i].first <= S && S <= pieces[i].second) {
            valid = true;
            break;
        }
    }

    if (!valid) {
        cout << 0;
        return 0;
    }

    // assuming that the range does indeed have something crossing S
    int range_end = S;
    for (int i = 0; i < N && range_end < E; i++) {
        if (pieces[i].first <= range_end + 1 && range_end < pieces[i].second) {
            range_end = max(range_end, pieces[i].second);
        }
    }

    cout << (range_end >= E);
    return 0;
}