#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<vector<int>> graph(N, vector<int>(N,0));

    while(true) {
        int a;
        int b;

        cin >> a >> b;
        
        if ( a == -1 ) {
            break;
        }

        graph[a][b] = 1;
    }

    for (auto row : graph) {
        for (auto elem : row) {
            cout << elem;
        }
        cout << '\n';
    }

    return 0;
}