#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

#define M 1000000007

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int ans = 1;
    int p = 2;
    while (n > 0) {
        if (n & 1) {
            ans = (ans * p) % M;
        }
        p *= p;
        p %= M;
        n >>= 1;
    }

    cout << ans;

    return 0;
}