#include <bits/stdc++.h>

#define int long long
#define endl '\n'
using namespace std;

#define M 1000000007LL

#define mod(a) ((a % M + M) % M)

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  // INPUTS
  // 1 <= N,Q <= 10^5
  int N, Q;
  cin >> N >> Q;
  vector<int> H(N);
  for (int i = 0; i < N; i++)
    cin >> H[i];
  sort(H.rbegin(), H.rend());

  // SORTING OUT COUNTER

  vector<pair<pair<int, int>, int>> counter;
  int current = 0;
  int count = 0;
  for (auto h : H) {
    if (h != current) {
      if (current != 0)
        counter.push_back({{current, h}, count});
      current = h;
    }
    count++;
  }
  counter.push_back({{current, 0}, count});

  // DEBUG

  // for (auto c : counter)
  //   cout << c.first.first << " " << c.first.second << " " << c.second << endl;
  // cout << endl;

  // CUMULATIVE SUM

  vector<int> throws;
  vector<int> cumsum;
  vector<int> height;
  vector<int> number;

  int r_throws = 0;
  int r_cumsum = 0;
  for (auto c : counter) {
    int start = c.first.first;
    int end = c.first.second;
    int count = c.second;

    r_throws += count * (start - end);
    throws.push_back(r_throws);
    r_cumsum += mod(count * (start - end) * (start + end + 1) / 2);
    r_cumsum %= M;
    cumsum.push_back(r_cumsum);
    height.push_back(end + 1);
    number.push_back(count);
  }

  // DEBUG

  // for (size_t i = 0; i < counter.size(); i++)
  //   cout << throws[i] << " " << cumsum[i] << " " << height[i] << " "
  //        << number[i] << endl;

  // cout << endl;

  // QUERIES

  for (size_t q = 0; q < Q; q++) {
    int T;
    cin >> T;

    T = min(T, throws[throws.size() - 1]);

    int i = 0;
    int jump = counter.size() - 1;
    while (jump > 0) {
      if (i + jump < counter.size() && throws[i + jump] <= T) {
        i += jump;
      } else {
        jump /= 2;
      }
    }

    if (T == throws[i]) {
      cout << cumsum[i] << endl;
      continue;
    }

    // cout << i << "BR" << endl;


    if(T > throws[i])
      i++;

    // cout << i << "AR" << endl;

    int blocks = mod((throws[i] - T) / number[i]);
    int blocksum =
        mod(number[i] * blocks * (height[i] + height[i] + blocks - 1) / 2);
    int individuals = mod((throws[i] - T) % number[i]);
    int individual_sum = mod(individuals * (height[i] + blocks));
    int cum = cumsum[i];
    // cout << cum << " " << blocksum << " " << individual_sum << endl;
    cout << mod(cum - blocksum - individual_sum) << endl;
  }

  return 0;
}