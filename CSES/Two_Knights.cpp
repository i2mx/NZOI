#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

int f(int n) {
    if (n == 1) return 0;
    if (n == 2) return 6;
    if (n == 3) return 28;
    if (n == 4) return 96;
    return (n * n * (n * n - 1)) / 2 - (4 * (n - 4) * (n - 4) + 20 * (n + 4) + 8 - 154 + 10);
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cout << f(i) << endl;
    }

    return 0;
}