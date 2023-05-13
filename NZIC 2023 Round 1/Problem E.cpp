#include <bits/stdc++.h>

using namespace std;

int main()
{
    map<int,vector<int>> lightrules;

    int N, D;
    cin >> N >> D;

    for (size_t i = 0; i < D; i++)
    {
        int k, p;
        cin >> k >> p;
        lightrules(k) = p;
    }


    for (size_t i = 0; i < N; i++)
    {
        int light = i+1;
        cout << lightrules.at(light);
    }
    

    return 0;
}