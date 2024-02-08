#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);

    char *str_number;
    cin >> str_number;

    // vector<int> digits_number;

    char *c = str_number;
    do
    {
        cout << (int)*c - 48;
    } while (*++c);

    return 0;
}