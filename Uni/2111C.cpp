#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        // where n <= 5e5
        // we do a sliding window approach on all the contiguous segments of the same
        int previous = -1;
        int g_min_cost = LONG_LONG_MAX;
        int l_min_cost;
        for (int i = 0; i < n; i++) {
            int ai;
            cin >> ai;
            // if (ai == previous) {
            //     l_min_cost -= ai;
            // }
            // else {
            //     l_min_cost = ai * (n - 1);
            // }
            l_min_cost = (ai == previous) ? l_min_cost - ai : ai * (n - 1);
            g_min_cost = min(l_min_cost, g_min_cost);
            previous = ai;
        }
        cout << g_min_cost << endl;
    }

    return 0;
}