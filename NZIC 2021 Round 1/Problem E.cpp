// Shocking Calculation
// https://train.nzoi.org.nz/problems/1204

// I fucking hate c++

#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    int hurts[10];
    for (size_t i = 0; i < 10; i++)
        cin >> hurts[i];

    int hurt_add;
    cin >> hurt_add;

    int hurt_mul;
    cin >> hurt_mul;

    int hurt_eql;
    cin >> hurt_eql;

    auto hurt = [hurts, hurt_add, hurt_mul](string s)
    {
        int value;
        value = 0;

        for (auto c : s)
        {
            switch (c)
            {
            case '+':
                value += hurt_add;
                break;
            case '*':
                value += hurt_mul;
                break;
            default:
                value += hurts[(int)c - 48];
                break;
            }
        }
        return value;
    };

   
    int min_cost = INT_MAX;

    for (int i = 1; i <= sqrt(N); i++)
    {
        for (int j = 1; j <= N / i ; j++)
        {   
            if(i*j>N){
                continue;
            }

            int cost = 0;

            if(i == 1 || j == 1) {
                cost += hurt(to_string(max(i,j)));
            }
            else {
                cost += hurt(to_string(i) + '*' + to_string(j));
            }

            if (i*j != N) {
                cost += hurt('+' + to_string(N-i*j));
            }


            min_cost = min(cost, min_cost);
        }
        
    }
    
    cout << min_cost + hurt_eql;

    return 0;
}
