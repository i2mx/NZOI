#include <bits/stdc++.h>

using namespace std;

long long threes(long long n)
{
    if (n <= 12)
    {
        return n >= 3;
    }

    long long p = log10(n);
    long long magnitude = pow(10,p);
    long long leading = n / magnitude;
    long long remaining = n - leading * magnitude;

    if (leading < 3) {
        return p*(magnitude)/10 * leading + threes(remaining);
    }

    if (leading == 3) {
        return p*(magnitude)/10 * leading + threes(remaining) + remaining + 1;
    }

    if (leading > 3) {
        return p*(magnitude)/10 * leading + threes(remaining) + magnitude;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long number;
    cin >> number;

    cout << threes(number);

    return 0;
}
