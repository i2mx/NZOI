#include <bits/stdc++.h>

// #define int long long
#define endl '\n'
using namespace std;

// N <= 2 * 10^5
// i'm assume the approach is greedy and if you have n you just remove n+1

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t, n, ai;
    int count, previous;
    cin >> t;
    while (t--) {
        cin >> n;

        count = 0;
        previous = -1;

        for (int i = 0; i < n; i++) {
            cin >> ai;
            if (ai <= previous + 1) continue;
            ++count;
            previous = ai;
        }

        cout << count << endl;
    }

    return 0;
}