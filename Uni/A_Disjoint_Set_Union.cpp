#include <bits/stdc++.h>
#include <atcoder/dsu>

#define int long long
#define endl '\n'
using namespace std;
using namespace atcoder;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;
    dsu uf(n);
    while (q--) {
        int type, a, b;
        cin >> type >> a >> b;
        if (type) cout << uf.same(a, b) << endl;
        else uf.merge(a, b);
    }

    return 0;
}