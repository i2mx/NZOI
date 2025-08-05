#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int x;
    for (int i = 0; i < (1 << n); i++) {
        x = (i ^ (i >> 1));
        for (int d = n - 1; d >= 0; d--) {
            cout << ((x & (1 << d)) != 0);
        }
        cout << endl;
    }

    return 0;
}