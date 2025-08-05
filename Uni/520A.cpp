#include <bits/stdc++.h>

// #define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;

    set<char> letters;

    cin >> n;
    cin >> s;

    for (auto c : s) {
        letters.insert(tolower(c));
        if (letters.size() >= 26) {
            cout << "YES";
            return 0;
        }
    }
    cout << "NO";

    return 0;
}