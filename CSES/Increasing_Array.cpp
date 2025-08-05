#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int floor = 0;
    int x = 0;
    int count = 0;
    for (int i = 0; i < n; i++) {
        cin >> x;
        if(x > floor) {
            floor = x;
        }
        else {
            count += floor - x;
        }
    }

    cout << count;

    return 0;
}