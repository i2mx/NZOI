#include <bits/stdc++.h>
#include <atcoder/convolution>

#define int long long
#define endl '\n'
using namespace std;
using namespace atcoder;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<int> a(n), b(m);

    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < m; i++) cin >> b[i];

    auto c = convolution(a, b);
    for (auto x : c) {
        cout << x << " ";
    }

    return 0;
}