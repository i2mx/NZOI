#include <bits/stdc++.h>

// #define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    if (s.length() < 7) {
        cout << "NO";
        return 0;
    }

    // we can now assume that there are atleast 7 things
    int count = s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6] - 7 * '0';

    if (count == 7 || count == 0) {
        cout << "YES";
        return 0;
    }

    for (int i = 0; i < s.length() - 7; i++) {
        count -= (s[i] - '0');
        count += (s[i + 7] - '0');
        if (count == 7 || count == 0) {
            cout << "YES";
            return 0;
        }
    }
    cout << "NO";
    return 0;
}