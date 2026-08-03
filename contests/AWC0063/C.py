"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < tired
"""
###################################################

# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
# MOD = 998244353
MOD = 1e9 + 7
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
    ダブリングみたいにかけていく
    l = [1, 2, 4, 8, ... ]を用意し
    Kより小さいものから左向きに
    ans =  ans * mx ** l[i] (MOD)
    をとる？

    K = 10^16
    ans = mx * 2 ** (4*10^16 + 6*10^16) % M
    ans

    """

    N, K = i_map()
    S = i_list()

    mx = max(S)
    l = [(2**i) % MOD for i in range(4 * 18)] # Sにかける数字を2倍ずつ保存して、大きいものから使っていく

    # print(l)
    for i in l[::-1]:
        if i <= K:
            break
    # print(i)
    ans1 = sum(S) - mx
    # iはKより小さい最大の数
    # ここから左向きに引いていく
    ans2 = mx
    # print(f"ans2={ans2}")
    i = len(l)-1
    while K:
        print(f"K={K}, i={i}")
        if l[i] <= K:
            ans2 = (ans2 * l[i]) % MOD
            K -= l[i]
            # print(f"ans2 * {2**l[i]} = {ans2}")
        i -= 1
        # print(K, i)
    # print("ans2", ans2)
    # print(f"ans = {ans1+ans2}")
    print(int(ans1 + ans2) % MOD)
        
    """
    各要素のMOD取った値を置いとく
    
    """



    return
######################################################

if __name__ == "__main__":
    main()