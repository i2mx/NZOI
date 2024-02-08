#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    multiset<string> socks;

    for (int i = 0; i < 7; i++)
    {
        string sock;
        cin >> sock;
        socks.insert(sock);
    }

    for (string sock : {"Red", "Blue", "Purple", "Pink"})
    {
        if (socks.count(sock) != 2)
        {
            cout << sock;
        }
    }

    return 0;
}