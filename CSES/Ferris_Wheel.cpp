#include <bits/stdc++.h>
#define int long long
#define endl '\n'
using namespace std;

/*
     /\_/\
   =( •.• )=      c++ competitive programming template.
     /   \
*/

#define all(a) (a).begin(), (a).end()
#define MOD 1000000007
#define INF LLONG_MAX

template <typename T>
ostream& operator<<(ostream& os, const pair<T, T>& p) {
    os << "(" << p.first << ", " << p.second << ")";
    return os;
}

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& v) {
    os << "[";
    for (int i = 0; i < v.size(); ++i) {
        os << v[i];
        if (i != v.size() - 1)
            os << ", ";
    }
    os << "]";
    return os;
}

/*
    (\_/)
    ( •_•)
    / >🚀       data structures and algorithms.
*/

int add(int a, int b) {
    return (a + b) % MOD;
}

int mul(int a, int b) {
    return (a * b) % MOD;
}

class union_find {
public:
    vector<int> parent, rank;

    union_find(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        iota(all(parent), 0);
    }

    int find(int i) {
        return parent[i] == i ? i : parent[i] = find(parent[i]);
    }

    bool unite(int x, int y) {
        int root_x = find(x);
        int root_y = find(y);

        if (root_x != root_y) {
            if (rank[root_x] < rank[root_y]) {
                parent[root_x] = root_y;
            }
            else if (rank[root_x] > rank[root_y]) {
                parent[root_y] = root_x;
            }
            else {
                parent[root_y] = root_x;
                rank[root_x]++;
            }
        }
        return root_x != root_y;
    }

    bool connected(int x, int y) {
        return find(x) == find(y);
    }
};

template <typename T>
class segment_tree {

private:
    T query(int start, int end, int node_start, int node_end, int node) {
        if (node_end < start || end < node_start) return id;
        if (start <= node_start && node_end <= end) return nodes[node];
        int mid = (node_start + node_end) / 2;
        T left = query(start, end, node_start, mid, 2 * node + 1);
        T right = query(start, end, mid + 1, node_end, 2 * node + 2);
        return combine(left, right);
    }

    void update(int index, T value, int node_start, int node_end, int node) {
        if (node_start == node_end) {
            nodes[node] = value;
            return;
        }
        int mid = (node_start + node_end) / 2;
        if (index <= mid) update(index, value, node_start, mid, 2 * node + 1);
        else update(index, value, mid + 1, node_end, 2 * node + 2);
        nodes[node] = combine(nodes[2 * node + 1], nodes[2 * node + 2]);
    }

    void build(const vector<T>& arr, int node_start, int node_end, int node) {
        if (node_start == node_end) {
            nodes[node] = arr[node_start];
            return;
        }
        int mid = (node_start + node_end) / 2;
        build(arr, node_start, mid, 2 * node + 1);
        build(arr, mid + 1, node_end, 2 * node + 2);
        nodes[node] = combine(nodes[2 * node + 1], nodes[2 * node + 2]);
    }

public:
    int n;
    vector<int> nodes;
    T id;
    function<T(T, T)> combine;

    segment_tree(int size, T identity, function<T(T, T)> combine) : id(identity), combine(combine) {
        n = size;
        nodes.resize(4 * n, 0);
    }

    T query(int start, int end) {
        if (start < 0 || end >= n || start > end) {
            throw out_of_range("Query range is out of bounds");
        }
        return query(start, end, 0, n - 1, 0);
    }

    void update(int index, T value) {
        if (index < 0 || index >= n) {
            throw out_of_range("Index is out of bounds");
        }
        update(index, value, 0, n - 1, 0);
    }

    void build(const vector<T>& arr) {
        if (arr.size() != n) {
            throw invalid_argument("Array size does not match segment tree size");
        }
        build(arr, 0, n - 1, 0);
    }
};

template <typename T = int>
T binary_exponent(T base, T id, int exponent, function<T(T, T)> combine) {
    T answer = id;
    T power = base;;
    while (exponent > 0) {
        if (exponent & 1) {
            answer = combine(answer, power);
        }
        exponent >>= 1;
        power = combine(power, power);
    }
    return answer;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, x;
    cin >> n >> x;

    vector<int> weight(n);
    for (int i = 0; i < n; ++i) {
        cin >> weight[i];
    }

    sort(all(weight));

    int start = 0;
    int end = n - 1;
    int count = 0;

    while (start <= end) {
        if (start == end) {
            count++;
            break;
        }

        if (weight[start] + weight[end] <= x) {
            start++;
            end--;
            count++;
        }

        else {
            count++;
            end--;
        }
    }

    cout << count << endl;
    return 0;
}