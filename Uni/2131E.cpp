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
        int n; cin >> n; vector<int> a(n), b(n);
        for (int i = 0; i < n; ++i) cin >> a[i];
        for (int i = 0; i < n; ++i) cin >> b[i];

        bool yes = true;
        for (int i = n - 1; i >= 0; --i) {
            if (a[i] == b[i]) continue;
            if (i != n - 1) {
                if ((a[i] ^ a[i + 1]) == b[i]) continue;
                if ((a[i] ^ b[i + 1]) == b[i]) continue;
            }
            cout << "NO" << endl;
            yes = false;
            break;
        }
        if (yes) cout << "YES" << endl;
    }

    return 0;
}