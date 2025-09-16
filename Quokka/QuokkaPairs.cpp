#include <bits/stdc++.h>
#include <unordered_set>

using namespace std;

signed main()
{
    int N, K;
    cin >> N >> K;
    unordered_set<int> nums;

    for (int i = 0; i < N; i++)
    {
        int x;
        cin >> x;

        if (nums.count(K - x)) {
            cout << "Y" << endl;
            return 0;
        }
        
        nums.insert(x);

    };

    cout << "N" << endl;
    return 0;
}
