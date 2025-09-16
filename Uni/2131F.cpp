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

    int t;
    cin >> t;
    while (t--) {
        int n; cin >> n;

        vector<pair<int, pair<int, int>>> pa(n);
        int total_1{}, total_0{};

        for (int i = 0; i < n; i++) {
            char c;
            cin >> c;
            if (c == '1') total_1++;
            else total_0++;
            pa[i] = { total_1 - total_0, {total_1, total_0} };
        }

        sort(all(pa));
        vector<int> differences(n);
        vector<int> partial1(n);
        vector<int> partial2(n);

        for (int i = 0; i < n; i++) {
            differences[i] = pa[i].first;
            if (i == 0) {
                partial1[i] = pa[i].second.first;
                partial2[i] = pa[i].second.second;
            }
            else {
                partial1[i] = partial1[i - 1] + pa[i].second.first;
                partial2[i] = partial2[i - 1] + pa[i].second.second;
            }
        }
        int overall_total = 0;
        total_1 = total_0 = 0;
        for (int i = 0; i < n; i++) {
            char c;
            cin >> c;
            if (c == '1') total_1++;
            else total_0++;
            int difference = total_1 - total_0;
            auto x = lower_bound(all(differences), -difference);
            auto pos = static_cast<int>(x - begin(differences));
            overall_total += total_1 * pos + total_0 * (n - pos);
            overall_total += pos == 0 ? 0 : partial1[pos - 1];
            overall_total += pos == 0 ? partial2[n - 1] : partial2[n - 1] - partial2[pos - 1];
        }
        cout << overall_total << endl;
    }
    return 0;
}