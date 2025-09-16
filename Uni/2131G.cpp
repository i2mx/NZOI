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
#define MOD 1000000007

map<int, int> memo;
// result of the calculation n^1 * (n-1)^2 * (n-3)^4 * ...
int g(int n) {
    if (memo.find(n) != memo.end()) return memo[n];
    int m = g(n - 1);
    return memo[n] = ((m * m % MOD) * n) % MOD;
}

// result of busting n to completion
int f(int n) {
    return (n * g(n - 1)) % MOD;
}
// number of operations needed to completely bust n
int inline cost(int n) {
    return n > 63 ? LLONG_MAX : (1LL << (n - 1));
}

int calculate(int n, int k) {
    int prod = 1;
    if (k-- > 0) prod *= n;
    // immediately pop n if we can afford it;
    int i = 0;
    while (k > 0) {
        i++;
        if (i > n) break;
        if (k >= cost(i)) {
            // if we can bust to completion we do it
            prod *= f(i);
            k -= cost(i);
        }
        else {
            // otherwise we have to call calculate again
            // prod *= calculate(i, k);
            // break;
            return (prod * calculate(i, k) % MOD);
        }
        prod %= MOD;
    }
    return prod % MOD;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    memo[0] = 1;
    memo[1] = 1;

    assert(f(5) == 2880);

    int t; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k;
        vector<int> s(n);
        for (int i = 0; i < n; ++i) cin >> s[i];
        sort(all(s));

        int prod = 1;
        for (int i = 0; i < n; ++i) {
            int x = s[i];
            if (cost(x) <= k) {
                prod *= f(x);
                prod %= MOD;
                k -= cost(x);
            }
            else {
                prod *= calculate(x, k);
                prod %= MOD;
                break;
            }
        }
        cout << prod << endl;
    }

    return 0;
}