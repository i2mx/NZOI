#include <bits/stdc++.h>

// #define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    transform(s.begin(), s.end(), s.begin(), [](char c) { return tolower(c); });

    for_each(s.begin(), s.end(), [](char c) {
        if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'y')
            return;
        cout << "." << c;
        });

    return 0;
}