#include <bits/stdc++.h>

using namespace std;

template <typename T>
ostream& operator<<(ostream& os, vector<T> v) {
    os << "[";
    for (int i = 0; i < v.size(); i++) {
        os << v[i];
        if (i != v.size() - 1) {
            os << ", ";
        }
    }
    os << "]";
    return os;
}

vector<int> smallestSubarrays(vector<int>& nums) {
    vector<int> distances(nums.size(), 1);
    for (int i = 0; i < 30; ++i) {
        int current = 0;
        for (int j = nums.size() - 1; j >= 0; --j) {
            if (nums[j] & (1 << i)) current = 1;
            if (current) distances[j] = max(distances[j], current++);
            else distances[j] = max(distances[j], 1);
        }
    }
    return distances;
}

signed main() {
    vector<int> v = { 1,0,2,1,3 };
    cout << smallestSubarrays(v);
}