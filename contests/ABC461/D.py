"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < give me higher rate point !!!!
"""
###################################################
import sys
# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
# MOD = 998244353
# drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


def c_list():
    return list(input().split())

from collections import defaultdict
from collections import Counter
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations

##################################################

def main():

    """
    H^2W^2はだめそう
    領域の総数は
    長さHのうち部分が (H * (H-1)) // 2 個
    とかは考えなくてよくて対角線だけ追うと
    HW*HWくらいあるってわかる。
    累積和を求めておいてHWかけて全部見ればいい？
    累積和へのqueryが(HW) ^ 2かかるので無理？

    縦横の1次元累積和とって,右下に配るDP
    無理そう

    Wについては全通り見るのはしょうがないので、それぞれについて
    H方向の累積和を取っておいて見る。
    ↑HW逆のほうが実装しやすそう
    0つづくから尺取りで左を動かせない

    W尺取りわからないが、辞書に左端からの和を入れていったら
    その時の和との差Kになるのが今までに何個でてきてたかで数えられる
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    H = int(input_data[0])
    W = int(input_data[1])
    K = int(input_data[2])
    
    S = [[0] * (W + 1) for _ in range(H + 1)]
    idx = 3
    for i in range(H):
        row = input_data[idx]
        idx += 1
        for j in range(W):
            S[i+1][j+1] = int(row[j]) + S[i][j+1] + S[i+1][j] - S[i][j]
    # for s in S:
    #     print(s)

    # 辞書より配列のほうが早い
    # すべてのHの範囲探索
    ans = 0
    dict = [0] * (H*W + 1)
    for u in range(H):
        for d in range(u, H):
            # ここでOWで合計が何個かを求めたい
            dict[0] = 1
            used = [0] # あとで0にする値
            for right in range(W):
                now = S[d+1][right+1] - S[u][right+1]
                find = now - K
                if 0 <= find :
                    ans += dict[find]
                dict[now] += 1
                used.append(now)
            for v in used:
                dict[v] = 0
    print(ans)

                        

    
    
    



    return
######################################################

if __name__ == "__main__":
    main()
