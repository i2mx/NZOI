#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

int node[4 * 200000];


int query(int lower, int upper, int n, int start, int end)
{
    if (lower <= start && end <= upper)
        return node[n];
    int mid = (start + end) / 2;
    int res = 0;

    if (lower <= mid)
        res = max(res, query(lower, upper, 2 * n, start, mid));
    if (mid + 1 <= upper)
        res = max(res, query(lower, upper, 2 * n + 1, mid + 1, end));

    return res;
}

void update(int x, int location, int n, int start, int end)
{
    if (start == end)
    {
        node[n] = x;
        return;
    }
    int mid = (start + end) / 2;
    if (location <= mid)
        update(x, location, 2 * n, start, mid);
    else
        update(x, location, 2 * n + 1, mid + 1, end);
    node[n] = max(node[2 * n], node[2 * n + 1]);
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    int heights[N];
    for (size_t i = 0; i < N; i++)
    {
        cin >> heights[i];
        update(heights[i], i, 1, 0, N-1);
    }

    int is_safe[N] = {false};
    int unsafes = 0;
    map<int, int> last_height;

    for (size_t i = 0; i < N; i++)
    {
        unsafes += 1;
        int h = heights[i];

        if (last_height.find(h) != last_height.end())
        {
            int last = last_height[h];
            int max_height = query(last, i, 1, 0, N-1);
            if (max_height <= h)
            {
                unsafes -= 1;
                is_safe[i] = true;
                if (!is_safe[last])
                {
                    unsafes -= 1;
                    is_safe[last] = true;
                }
            }
        }

        last_height[h] = i;

        cout << unsafes << endl;
    }
    

    
    


    return 0;
}