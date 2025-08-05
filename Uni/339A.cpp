#include <bits/stdc++.h>

// #define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    multiset<int> digits;

    for (int i = 0; i < s.length(); i += 2) {
        digits.insert(s[i]);
    }

    auto it = digits.begin();
    while (it != digits.end()) {
        cout << (char)*it;
        if (++it != digits.end()) {
            cout << "+";
        }
    }

    return 0;
}