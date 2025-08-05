#include <bits/stdc++.h>

// #define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    cin >> a >> b;

    transform(begin(a), end(a), begin(a), [](char c) {
        return tolower(c);
        });

    transform(begin(b), end(b), begin(b), [](char c) {
        return tolower(c);
        });

    int output = 0;

    for (int i = 0; i < a.length(); i++) {
        if (a[i] > b[i]) {
            output = 1;
            break;
        }
        if (a[i] < b[i]) {
            output = -1;
            break;
        }
    }

    cout << output;
    return 0;
}