#include <bits/stdc++.h>

// #define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int w;
    cin >> w;

    cout << ((w & 1 | w == 2) ? "NO" : "YES");
}