#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    for(int i = 0; i < N; i++) {
        cin >> skipws;

        int x;
        int y;

        cin >> x >> y;

        vector<string> rows;
        map<pair<int,int>, pair<int,int>> parent;

        pair<int,int> start;
        pair<int,int> end;


        for (int j = 0; j <= y; j++) {
            string s;

            cin >> noskipws;    
            cin >> s;
            cout << s;

            rows.push_back(s);

            for(int k = 0; k < x; k++) {
                // cout << s[k];

                if (s[k] == 'S') {
                    start = make_pair(j,k);
                }
                if (s[k] == 'E') {
                    end = make_pair(j,k);
                }
            }

            cout << endl;

        }

        // cout << start.first << start.second << end.first << end.second;

    }


    return 0;
}