#include <bits/stdc++.h>
#include <atcoder/scc>

#define int long long
#define endl '\n'
using namespace std;
using namespace atcoder;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    scc_graph sg(n);
    while (m--) {
        int a, b;
        cin >> a >> b;
        sg.add_edge(a, b);
    }
    auto connected_components = sg.scc();

    cout << connected_components.size() << endl;
    for (auto cc : connected_components) {
        cout << cc.size() << " ";
        for (auto c : cc) {
            cout << c << " ";
        }
        cout << endl;
    }


    return 0;
}