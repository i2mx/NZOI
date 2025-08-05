#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    int letters[26] = { 0 };
    for (auto c : s) {
        letters[c - 'A']++;
    }

    int count = 0;
    char middle;

    for (int i = 0; i < 26; i++) {
        if (letters[i] % 2 == 1) {
            count++;
            middle = i;
            if (count == 2) {
                cout << "NO SOLUTION";
                return 0;
            }
        }
    }

    for (int i = 0; i < 26; i++) {
        for (int j = 0; j < letters[i] / 2; j++) {
            cout << (char)('A' + i);
        }
    }

    if (count == 1) {
        cout << (char)('A' + middle);
    }

    for (int i = 25; i >= 0; i--) {
        for (int j = 0; j < letters[i] / 2; j++) {
            cout << (char)('A' + i);
        }
    }




    return 0;
}