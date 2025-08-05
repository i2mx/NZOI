#include <bits/stdc++.h>

// #define int long long
#define endl '\n'
using namespace std;


int cubes(int n) {
    return ((n + 2) * (n + 1) * n) / 6;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    int x = 0;
    int d = 100;
    while (d > 0) {
        if (cubes(x + d) <= N) {
            x += d;
        }
        else {
            d /= 2;
        }
    }

    cout << x;
    return 0;
}