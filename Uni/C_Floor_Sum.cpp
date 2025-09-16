#include <bits/stdc++.h>
#include <atcoder/math>

#define int long long
#define endl '\n'
using namespace std;
using namespace atcoder;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n, m, a, b;
        cin >> n >> m >> a >> b;

        floor_sum(n, m, a, b);
        int result = floor_sum(n, m, a, b);

        cout << result << endl;
    }

    return 0;
}