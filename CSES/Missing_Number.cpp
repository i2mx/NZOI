#include <bits/stdc++.h>

// #define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int x = 0;
    for (int i = 1; i <= n; i++) {
        x ^= i;
    }

    int y;
    for (int i = 1; i < n; i++) {
        cin >> y;
        x ^= y;
    }

    cout << x;

    return 0;
}