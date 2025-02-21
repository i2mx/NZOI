#include <bits/stdc++.h>

using namespace std;

signed main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    sort(A.begin(), A.end());

    int prev = 31230912838123122312;
    int total = 0;
    for(auto a : A) {
        if (prev != a) 
            total++;
        prev = a;
    }

    cout << total;

    return 0;
}