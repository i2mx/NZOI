#include <bits/stdc++.h>
#include <atcoder/fenwicktree>

#define int long long
#define endl '\n'
using namespace std;
using namespace atcoder;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;

    fenwick_tree<int> ft(n);

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        ft.add(i, x);
    }

    while (q--) {
        int type, x, y;
        cin >> type >> x >> y;
        if (!type) ft.add(x, y);
        else cout << ft.sum(x, y) << endl;
    }
    return 0;
}