#include <bits/stdc++.h>

// #define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    if (n == 1) {
        cout << "1";
        return 0;
    }

    if (n <= 3) {
        cout << "NO SOLUTION";
        return 0;
    }

    if (n == 4) {
        cout << "3 1 4 2"; 
        return 0;
    }

    for (size_t i = 1; i <= n; i += 2) {
        cout << i << " ";
    }

    for (size_t i = 2; i <= n; i += 2) {
        cout << i << " ";
    }


    return 0;
}