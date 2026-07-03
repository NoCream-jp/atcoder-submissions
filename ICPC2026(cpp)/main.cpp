#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using vi = vector<ll>;
using vll = vector<ll>;
using vvi = vector<vector<ll>>;
using vvll = vector<vector<ll>>;
using vs = vector<string>;
using pii = pair<ll, ll>;
using pll = pair<ll, ll>;
using uset = unordered_set<ll>;
using umap = unordered_map<ll, ll>;


const int MOD = 998244353;
const ll INF = 1LL << 60;
const int drct[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()

// --------------------------------------------------------
void yesno(bool b) {
  cout << (b ? "Yes" : "No") << endl;
}

template <typename T>
void printVec(const T& arr) {
  for (const auto& e : arr) {
      cout << e << " ";
  }
  cout << "\n";
}

template <typename T>
void printGrid(const vector<vector<T>>& arr) {
  for (const auto& e : arr) {
      printVec(e);
  }
}
// --------------------------------------------------------

ll solve() {
  cin.tie(nullptr);
  ios::sync_with_stdio(false);


  return 0;
}

int main() {
  solve();
  return 0;
}