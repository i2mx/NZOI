#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

void hanoi(int n, int a, int b, int c) {
    if (n == 0) return;
    hanoi(n - 1, a, c, b);
    cout << a << " " << c << endl;
    hanoi(n - 1, b, a, c);
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; cin >> n;

    cout << (1 << n) - 1 << endl;
    hanoi(n, 1, 2, 3);

    return 0;
}