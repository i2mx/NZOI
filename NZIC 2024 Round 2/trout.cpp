#include <bits/stdc++.h>

#define int long long
// #define endl '\n'
using namespace std;

// downstream graph
vector<list<pair<int, int>>> downstream(100000);
// upstream graph
vector<list<pair<int, int>>> upstream(100000);

// number of trout that can be found at a point
vector<int> number(100000, 0);

void update(int point, int distance) {
        for(auto parent : upstream[point]) {
            if(parent.first <= distance) {
                number[parent.second]++;
        }
    }
}

int query(int point, int distance) {
    int count = number[point];
    
    for(auto child : downstream[point]) {
        if(child.first <= distance) {
            count += query(child.second, distance - child.first);
        }
    }
    return count;
}

signed main() {
    // cout << "hello world";

    // points, trouts, events, trouts discovered
    int N, M, K, U;
    cin >> N >> M >> K >> U;

    // the river is a tree graph that has a list of points that a flows to 
    for (int i = 0; i < N - 1; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        downstream[a].push_back({w, b});
    }

    // queue<int> q;
    // q.push(0);
    // while(!q.empty()) {
    //     int current = q.front();
    //     upstream[current].push_back({0, current});
    //     q.pop();
    //     for(auto child : downstream[current]) {
    //         q.push(child.second);
    //         for (auto parent : upstream[current]) {
    //             upstream[child.second].push_back({child.first + parent.first, parent.second});
    //         }
    //     }
    // }

    // for(auto point : upstream) {
    //     for(auto parent : point) {
    //         cout << parent.first << " ";
    //     }
    //     cout << endl;
    // }

    for (size_t i = 0; i < M; i++)
    {
        int L, S;
        cin >> L >> S;
        number[L] += S;
    }



    for (size_t i = 0; i < K; i++)
    {
        char query;
        cin >> query;
        if(query == 'Q') {
            int L;
            cin >> L;
            cout << query(L) << endl;
        } else {
            int L, S;
            cin >> L >> S;
            number[L] += S;
        }
    }
    

    return 0;
}