#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;

    vector<int> applicants(n);
    for (int i = 0; i < n; i++) {
        cin >> applicants[i];
    }

    vector<int> apartments(m);
    for (int i = 0; i < m; i++) {
        cin >> apartments[i];
    }

    sort(applicants.begin(), applicants.end());
    sort(apartments.begin(), apartments.end());

    int count = 0;

    int i = 0;
    int j = 0;

    while (i < n && j < m) {
        if (apartments[j] > applicants[i] + k) {
            i++;
            continue;
        }

        if (applicants[i] > apartments[j] + k) {
            j++;
            continue;
        }

        count++;
        i++;
        j++;
    }

    cout << count;

    return 0;
}