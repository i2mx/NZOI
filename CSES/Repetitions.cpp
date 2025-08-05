#include <bits/stdc++.h>

// #define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    int max_n = 0;
    int n = 0;
    char pc = ' ';

    for (auto c : s) {
        if (pc == c) {
            n += 1;
        }
        else {
            n = 1;
        }
        max_n = max(max_n, n);
        pc = c;
    }

    cout << max_n;

    return 0;
}