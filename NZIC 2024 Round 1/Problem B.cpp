#include <bits/stdc++.h>

#define int long long
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int A,B,K;
    cin >> A >> B >> K;

    // B for bigger
    if (A > B) swap(A, B);

    pair<int, int> mini = {K, 0};

    for (int x = 0; x <= 2*B; x++)
    {
        int y1 = ( K - x*A ) / B;
        int d1 = abs(x*A + y1*B - K);

        if(y1 >= 0) mini = min(mini, {d1, x + y1});

        int y2 = y1+1;
        int d2 = abs(x*A + y2*B - K);

        mini = min(mini, {d2, x + y2});
    }
    cout << mini.first << " " << mini.second << endl;
    return 0;
}