#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++){
            cout << (i ^ j) << " ";
        }
        cout << endl;
    }

    return 0;
}