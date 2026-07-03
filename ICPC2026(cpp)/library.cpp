#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// ======================================================================
// 1. 数学系・素数・約数
// ======================================================================

// l~rのうち、nで割り切れるものの個数
ll get_division(ll left, ll right, ll n) {
    ll r_count = right / n;
    ll l_count = (left - 1) / n; // leftの1つ前まで引く
    return r_count - l_count;
}

// 素数列挙 (エラトステネスの篩: 0 から right までの素数列挙)
vector<int> get_primes(int right) {
    vector<bool> is_prime(right + 1, true);
    vector<int> primes;
    if (right >= 0) is_prime[0] = false;
    if (right >= 1) is_prime[1] = false;
    for (int i = 2; i <= right; i++) {
        if (is_prime[i]) {
            primes.push_back(i);
            for (int j = i * 2; j <= right; j += i) {
                is_prime[j] = false;
            }
        }
    }
    return primes;
}

// 最大公約数・最小公倍数
// ※ C++17以降は標準ライブラリ <numeric> に std::gcd(a, b), std::lcm(a, b) があります。
// 例: ll g = gcd(12, 18); // -> 6

// ユークリッド距離
double get_dist(double x1, double y1, double x2, double y2) {
    return std::hypot(x2 - x1, y2 - y1);
}

// 繰り返し二乗法 (a^n % mod)
ll modpow(ll a, ll n, ll mod = 998244353) {
    ll res = 1;
    a %= mod;
    while (n > 0) {
        if (n & 1) res = res * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return res;
}

// 素因数列挙
vector<ll> prime_factors(ll n) {
    vector<ll> res;
    for (ll i = 2; i * i <= n; i++) {
        while (n % i == 0) {
            res.push_back(i);
            n /= i;
        }
    }
    if (n > 1) res.push_back(n);
    return res;
}

// ======================================================================
// 2. 配列操作・文字列
// ======================================================================

// 時計回りに回転 (N x M のグリッド)
vector<string> rotate(const vector<string>& grid) {
    if(grid.empty()) return {};
    int H = grid.size(), W = grid[0].size();
    vector<string> res(W, string(H, ' '));
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            res[j][H - 1 - i] = grid[i][j];
        }
    }
    return res;
}

// 累積和構築
template<typename T>
vector<T> cum_sum(const vector<T>& v) {
    vector<T> res(v.size() + 1, 0);
    for (size_t i = 0; i < v.size(); i++) {
        res[i + 1] = res[i] + v[i];
    }
    return res;
}

// Z-Algorithm
vector<int> z_algo(const string& S) {
    int n = S.size();
    vector<int> A(n, 0);
    A[0] = n;
    int i = 1, j = 0;
    while (i < n) {
        while (i + j < n && S[j] == S[i + j]) j++;
        A[i] = j;
        if (j == 0) {
            i++;
            continue;
        }
        int k = 1;
        while (i + k < n && k + A[k] < j) {
            A[i + k] = A[k];
            k++;
        }
        i += k;
        j -= k;
    }
    return A;
}

// 最長増加部分列 (LIS) の長さ
template<typename T>
int lis(const vector<T>& a) {
    vector<T> dp;
    for (const auto& x : a) {
        auto it = lower_bound(dp.begin(), dp.end(), x);
        if (it == dp.end()) dp.push_back(x);
        else *it = x;
    }
    return dp.size();
}

// ランレングス圧縮 (RLE)
// 戻り値: pair<値, 連続する長さ> のリスト
template<typename T>
vector<pair<T, int>> RLE(const vector<T>& seq) {
    vector<pair<T, int>> res;
    if (seq.empty()) return res;
    T current = seq[0];
    int count = 1;
    for (size_t i = 1; i < seq.size(); i++) {
        if (seq[i] == current) count++;
        else {
            res.push_back({current, count});
            current = seq[i];
            count = 1;
        }
    }
    res.push_back({current, count});
    return res;
}

// 二分探索 (bisect)
// C++では std::lower_bound(all(A), x) と std::upper_bound(all(A), x) を使います。
// 例: int index = lower_bound(A.begin(), A.end(), x) - A.begin();

// 辞書・カウント (Counter)
// C++では std::map や std::unordered_map を使います。
// 例: map<int, int> count; for(int x : A) count[x]++;

// ======================================================================
// 3. グラフ・木構造
// ======================================================================

// BFS
// int H, W;
// dist[sy][sx] = 0;
//     que.push({sy, sx});

//     // 4. BFS（幅優先探索）の実行
//     while (!que.empty()) {
//         // キューの先頭要素を取り出し、削除する
//         auto [y, x] = que.front(); // C++17の構造化束縛を使用
//         que.pop();

//         // 上下左右の4方向を探索
//         for (int dir = 0; dir < 4; ++dir) {
//             int ny = y + dy[dir];
//             int nx = x + dx[dir];

//             // 探索のスキップ条件
//             // 条件1: グリッドの範囲外にはみ出している
//             if (ny < 0 || ny >= H || nx < 0 || nx >= W) continue;
            
//             // 条件2: 移動先が壁（'#'）である
//             if (grid[ny][nx] == '#') continue;
            
//             // 条件3: 既に訪問済みである（最短距離が確定している）
//             if (dist[ny][nx] != -1) continue;

//             // すべての条件をクリアした場合、距離を書き込んでキューに追加
//             dist[ny][nx] = dist[y][x] + 1;
//             que.push({ny, nx});
//         }
//     }

// ワーシャルフロイド法
void floyd(vector<vector<ll>>& dist, int N) {
    for (int k = 0; k < N; k++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(dist[i][k] != INF && dist[k][j] != INF) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
}

// Union-Find
struct UnionFind {
    vector<int> parents;
    UnionFind(int n) : parents(n, -1) {}
    
    int find(int x) {
        if (parents[x] < 0) return x;
        return parents[x] = find(parents[x]);
    }
    
    bool unite(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) return false;
        if (parents[x] > parents[y]) swap(x, y);
        parents[x] += parents[y];
        parents[y] = x;
        return true;
    }
    
    int size(int x) {
        return -parents[find(x)];
    }
    
    bool same(int x, int y) {
        return find(x) == find(y);
    }
};

// ======================================================================
// 4. データ構造・高度なアルゴリズム
// ======================================================================

// 二次元累積和
struct PrefixSum2D {
    int H, W;
    vector<vector<ll>> S;
    PrefixSum2D(const vector<vector<ll>>& grid) {
        H = grid.size();
        W = (H > 0) ? grid[0].size() : 0;
        S.assign(H + 1, vector<ll>(W + 1, 0));
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                S[i + 1][j + 1] = grid[i][j] + S[i][j + 1] + S[i + 1][j] - S[i][j];
            }
        }
    }
    // [r1, r2], [c1, c2] の閉区間の和を返す
    ll query(int r1, int c1, int r2, int c2) {
        if (r1 > r2 || c1 > c2) return 0;
        r1 = max(0, r1); c1 = max(0, c1);
        r2 = min(H - 1, r2); c2 = min(W - 1, c2);
        return S[r2 + 1][c2 + 1] - S[r1][c2 + 1] - S[r2 + 1][c1] + S[r1][c1];
    }
};

// セグメント木 (非再帰版 1-indexed)
template<typename T>
struct SegmentTree {
    int n;
    vector<T> tree;
    T id_ele;
    function<T(T, T)> f;
    
    SegmentTree(int _n, function<T(T, T)> _f, T _id) : f(_f), id_ele(_id) {
        n = 1;
        while (n < _n) n *= 2;
        tree.assign(2 * n, id_ele);
    }
    
    void build(const vector<T>& v) {
        for(size_t i = 0; i < v.size(); i++) tree[n + i] = v[i];
        for(int i = n - 1; i > 0; i--) tree[i] = f(tree[i * 2], tree[i * 2 + 1]);
    }
    
    void update(int k, T x) {
        k += n;
        tree[k] = x;
        while (k > 1) {
            k >>= 1;
            tree[k] = f(tree[2 * k], tree[2 * k + 1]);
        }
    }
    
    // [l, r) の半開区間のクエリ
    T query(int l, int r) {
        l += n; r += n;
        T res = id_ele;
        while (l < r) {
            if (l & 1) res = f(res, tree[l++]);
            if (r & 1) res = f(res, tree[--r]);
            l >>= 1; r >>= 1;
        }
        return res;
    }
};

// Trie木 (英小文字専用)
struct TrieNode {
    vector<int> children;
    bool is_end;
    TrieNode() : children(26, -1), is_end(false) {}
};
struct Trie {
    vector<TrieNode> nodes;
    Trie() { nodes.push_back(TrieNode()); }
    
    void insert(const string& word) {
        int curr = 0;
        for (char ch : word) {
            int c = ch - 'a';
            if (nodes[curr].children[c] == -1) {
                nodes[curr].children[c] = nodes.size();
                nodes.push_back(TrieNode());
            }
            curr = nodes[curr].children[c];
        }
        nodes[curr].is_end = true;
    }
    
    bool search(const string& word) {
        int curr = 0;
        for (char ch : word) {
            int c = ch - 'a';
            if (nodes[curr].children[c] == -1) return false;
            curr = nodes[curr].children[c];
        }
        return nodes[curr].is_end;
    }
};

// ローリングハッシュ
struct RollingHash {
    int n;
    vector<unsigned long long> prefix, power;
    const unsigned long long b = 3491;
    const unsigned long long m = 999999937;
    
    RollingHash(const string& S) {
        n = S.size();
        prefix.assign(n + 1, 0);
        power.assign(n + 1, 1);
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = (prefix[i] * b + S[i]) % m;
            power[i + 1] = (power[i] * b) % m;
        }
    }
    // [l, r) の半開区間
    unsigned long long get(int l, int r) {
        unsigned long long res = (prefix[r] + m - (power[r - l] * prefix[l]) % m) % m;
        return res;
    }
};
