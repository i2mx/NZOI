// Mind Reader https://train.nzoi.org.nz/problems/1218

#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<string> numbers {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"};
    vector<string> suits = {"spades", "clubs", "diamonds", "hearts"};

    string number;
    cin >> number;
    
    string suit;
    cin >> suit;

    vector<string>::iterator i = find(suits.begin(), suits.end(), suit);
    vector<string>::iterator j = find(numbers.begin(), numbers.end(), number);

    cout << 13 * (distance(i, suits.end()) - 1) + (distance(j, numbers.end()) - 1);

    return 0;
}