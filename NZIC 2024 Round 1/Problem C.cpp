#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // 1 <= N <= 1000
    int N;
    cin >> N;
    vector<int> A(N);
    vector<int> B(N);
    for (size_t i = 0; i < N; i++) cin >> A[i];
    for (size_t i = 0; i < N; i++) cin >> B[i];    

    vector<int> alignments;
    for (size_t i = 0; i < N; i++) {
        for (size_t j = 0; j < N; j++) {
            alignments.push_back(A[i] - B[j]);
        }
    }

    sort(alignments.begin(), alignments.end());

    int best = 0;
    int current = 69;
    int count = 0;
    for (auto a : alignments) { 
        if(a==current) count ++;
        else {
            current = a;
            count = 1;
        }
        best = max(best, count);
    }

    cout << 2 * N - best;

    return 0;
}