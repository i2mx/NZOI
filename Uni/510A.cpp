#include <bits/stdc++.h>

// #define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            for (int i = 0; i < m; i++)
            {
                cout << "#";
            }
        }
        else if (i % 4 == 1) {
            for (int i = 1; i < m; i++) {
                cout << ".";
            }
            cout << "#";
        }
        else {
            cout << "#";
            for (int i = 1; i < m; i++) {
                cout << ".";
            }
        }
        cout << endl;
    }

    return 0;
}