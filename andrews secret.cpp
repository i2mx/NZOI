#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int x;
  int smallest = INT_MAX;
  int biggest = INT_MIN;
  int total = 0;

  for (int i = 0; i < 100; i++) {
    cin >> x;
    if (x < smallest)
      smallest = x;
    if (x > biggest)
      biggest = x;
    total += x; } 
    
    cout << smallest << " " << biggest << " " << total / 100;

  return 0;
}