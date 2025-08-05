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
        int x, y;
        cin >> y >> x; 

        int layer = max(x,y);
        if (layer % 2 == 0) {
            swap(x, y);
        }

        if (x == layer) {
            cout << layer * layer + 1 - y << endl;
        }

        else {
            cout << (layer - 1) * (layer - 1) + x << endl; 
        }
    }
    return 0;
}