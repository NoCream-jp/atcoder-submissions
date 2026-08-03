"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < keep thinking
"""
###################################################

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
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations as p

##################################################


def main():
    """
    bit全探索っぽい
    各数字について
    j桁目が立ってるとして全スキャン結果と照合して矛盾がないか見る
    """

    
    N, M = i_map()

    l = [0 for i in range(N)]

    scan = [i_list() for i in range(M)]
    ans = float('inf')
    for i in range(2**N):
        flag = True # 矛盾がなければTrue
        for jj in range(M):
            # print(f"数字{i}についてscan{jj}番目{scan[jj]}を適用する")
            K = scan[jj][0]
            R = scan[jj][-1]
            if R: # 1のとき
                tmp = 0 # 判定を足していく
                # print(f"R={R}なので合計が0ならアウト",end=" ")
                for k in range(K): # 全scanのパターンシフトした時に0ならアウト
                    checkindex = scan[jj][k+1]-1
                    # print(f"ビット立ってるかどうか判定{i}の{checkindex}シフト目　{(i << checkindex) & 1}")
                    tmp += (i >> checkindex) & 1
                if tmp == 0:
                    # print(f"tmp={tmp}なのでアウト")
                    flag = False
            else: # 0のとき
                # print(f"R={R}なのでひとつでも1があればアウト", end=" ")
                for k in range(K): # kシフトしたときに1ならアウト
                    checkindex = scan[jj][k+1]-1
                    if ((i << checkindex) & 1) == True:
                        # print("アウト")
                        flag = False
        if flag:
            # print(f"flag = {flag}")
            ans = min(ans, i.bit_count())
        # print("ans", ans)
        # print()
    print(ans)

    return
######################################################

if __name__ == "__main__":
    main()
