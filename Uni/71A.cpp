#include <bits/stdc++.h>

// #define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    string s;
    while(N--) {
        cin >> s;
        if(s.length() > 10) {
            cout << s.front() << s.length() - 2 << s.back() << endl;
        }
        else {
            cout << s << endl;
        }
    }


    return 0;
}