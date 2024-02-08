#include <bits/stdc++.h>
using namespace std;

signed main()
{
    int N;
    cin >> N;

    vector<int> disjoint;
    for (size_t i = 0; i < N; i++)
    {
        disjoint.push_back(i);
    }

    int a;
    int b;
    while (cin >> a >> b && a != -1)
    {
        if (disjoint[a] == disjoint[b])
            continue;

        int x = min(disjoint[a], disjoint[b]);
        int y = max(disjoint[a], disjoint[b]);

        for (size_t i = 0; i < N; i++)
        {
            if (disjoint[i] == y)
            {
                disjoint[i] = x;
            }
        }
    }

    int count = 0;

    for (size_t i = 0; i < N; i++)
    {
        bool found = false;
        for (size_t j = 0; j < N; j++)
        {
            if (disjoint[j] == i)
            {
                if (!found)
                {
                    cout << ++count << ": ";
                    found = true;
                }
                cout << j << " ";
            }
        }
        if (found) cout << '\n';
    }
}