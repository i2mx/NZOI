// Shocking Calculation
// https://train.nzoi.org.nz/problems/1204

// I fucking hate c++

#include <bits/stdc++.h>

using namespace std;

int eval(string s)
{
    if (s.find('+') == -1 && s.find('*') == -1)
    {
        return stoi(s);
    }

    if (s.find('+') != -1)
    {
        int p = s.find('+');
        return eval(s.substr(0, p)) + eval(s.substr(p + 1));
    }

    int m = s.find('*');
    return eval(s.substr(0, m)) * eval(s.substr(m + 1));
};

void print(vector<string> v)
{
    for (string var : v)
    {
        cout << var << ", ";
    }
    cout << '\n';
}

vector<string> extend(string s)
{
    vector<string> new_strings;

    if (s.empty())
    {
        for (char i = '1'; i <= '9'; i++)
            new_strings.push_back(s + i);
        return new_strings;
    }

    for (char i = '0'; i <= '9'; i++)
    {
        new_strings.push_back(s + i);
        if (i != '0')
        {
            if (s.find('+') == -1)
            {
                new_strings.push_back(s + '+' + i);
            }
            if (s.find('*') == -1)
            {
                new_strings.push_back(s + '*' + i);
            }
        }
    }

    return new_strings;
}

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
            // cout << c << '\n';
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
            // cout << value << '\n';
        }
        return value;
    };

    auto hurt_comp = [hurt](string a, string b)
    {
        if (hurt(a) == hurt(b))
        {
            return eval(a) < eval(b);
        }
        return hurt(a) > hurt(b);
    };


    priority_queue<string, vector<string>, function<bool(string, string)>> pq(hurt_comp);
    pq.push("1");
    pq.push("2");
    pq.push("3");
    pq.push("4");
    pq.push("5");
    pq.push("6");
    pq.push("7");
    pq.push("8");
    pq.push("9");

    while (pq.size())
    {
        string s = pq.top();
        pq.pop();

        if (eval(s) > N)
        {
            continue;
        }

        if (eval(s) == N)
        {
            cout << hurt(s) + hurt_eql << '\n';
            break;
        }

        for (auto ss : extend(s))
        {
            pq.push(ss);
        }

        // print(hq);
        // cout << s << "  " << hurt(s) << '\n';
    }
    

    return 0;
}
