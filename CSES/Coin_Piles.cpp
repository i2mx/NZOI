#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    int a, b;
    while (t--) {
        cin >> a >> b;
        if ((a + b) % 3 != 0) {
            cout << "NO" << endl;
        }
        else if (max(a, b) > 2 * min(a, b)) {
            cout << "NO" << endl;
        }
        else {
            cout << "YES" << endl;
        }
    }

    return 0;
}