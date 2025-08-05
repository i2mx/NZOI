#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int total = 0;
    while (n > 0) {
        total += n / 5;
        n /= 5;
    }

    cout << total;

    return 0;
}