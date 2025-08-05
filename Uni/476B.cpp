#include <bits/stdc++.h>

// #define int long long
// #define endl '\n'
using namespace std;

int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}

int C(int n, int r) {
    return (r < 0 || r > n) ? 0 : factorial(n) / factorial(n - r) / factorial(r);
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    cin >> a >> b;

    int x = 0;
    for (auto c : a) {
        if (c == '+') {
            x += 1;
        }
        else {
            x -= 1;
        }
    }


    int y = 0;
    int n = 0;
    for (auto c : b) {
        if (c == '+') {
            y += 1;
        }
        else if (c == '-') {
            y -= 1;
        }
        else {
            n += 1;
        }
    }

    int d = abs(x - y);
    // cout << n << d;
    if (d % 2 != n % 2) {
        cout << "0.000000000000";
        return 0;
    }

    cout << setprecision(12) << (double) C(n, (n - d) / 2) / pow(2, n);
    return 0;
}
