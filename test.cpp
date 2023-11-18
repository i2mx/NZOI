#include <bits/stdc++.h>

using namespace std;

int sub_of_max_sub_array(vector<int> arr) {
    int local_max = 0;
    int global_max = 0;

    for (auto &&i : arr)
    {
        local_max = max(i, local_max + i);
        global_max = max(local_max, global_max);
    }

    return global_max;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> arr = {-1,2,4,-5,1,2,4};
    cout << sub_of_max_sub_array(arr);
    return 0;

    
}