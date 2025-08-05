#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    if (n % 4 == 0) {
        cout << "YES" << endl;
        cout << n / 2 << endl;
        for (int i = 1; i <= n; i++) {
            if (i % 4 == 1 || i % 4 == 0) {
                cout << i << " ";
            }
        }
        cout << endl;
        cout << n / 2 << endl;
        for (int i = 1; i <= n; i++) {
            if (i % 4 == 2 || i % 4 == 3) {
                cout << i << " ";
            }
        }
    }

    else if (n % 4 == 3) {
        cout << "YES" << endl;
        cout << n / 2 + 1 << endl;
        cout << "1 2 ";
        for (int i = 4; i <= n; i++) {
            if (i % 4 == 3 || i % 4 == 0) {
                cout << i << " ";
            }
        }
        cout << endl;
        cout << n / 2 << endl;
        cout << "3 ";
        for (int i = 4; i <= n; i++) {
            if (i % 4 == 1 || i % 4 == 2) {
                cout << i << " ";
            }
        }
    }

    else {
        cout << "NO";
    }

    return 0;
}