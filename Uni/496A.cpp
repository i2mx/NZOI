#include <bits/stdc++.h>

// #define int long long
// #define endl '\n'
using namespace std;

signed main() {
    // ios_base::sync_with_stdio(false);
    // cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    for (int i = 0; i < n - 1; i++) {
        nums[i] = nums[i + 1] - nums[i];
    }

    nums.pop_back();
    int d = *max_element(begin(nums), end(nums));
    int d2 = INT_MAX;
    for (int i = 0; i < n - 1; i++) {
        d2 = min(d2, nums[i] + nums[i + 1]);
    }

    cout << max(d, d2);

    return 0;
}