"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < wanna solve green
"""
###################################################
# import sys
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
    ab_ でcに置き換える
    a_c でbに置き換える
    _bc でaに置き換える

    その逆でabcのどれかを個おtなるものに変更してしまう

    しか変動しない
    連続部分列なので、それ以外の場所に影響はない
    """

    N, Q = i_map()
    S = list(input())

    ans = 0
    for i in range(1, N-1):
        if (S[i-1], S[i], S[i+1]) == ("A", "B", "C"):
            ans += 1

    for _ in range(Q):
        x, c = input().split()
        x = int(x) - 1

        # 破壊
        if (0 <= x-2) and (S[x-2], S[x-1], S[x]) == ("A", "B", "C") and c != "C":
            ans -= 1
        if (0 <= x-1 and x+1 <= N-1) and (S[x-1], S[x], S[x+1]) == ("A", "B", "C") and c != "B":
            ans -= 1
        if (x+2 <= N-1) and (S[x], S[x+1], S[x+2]) == ("A", "B", "C") and c != "A":
            ans -= 1
        
        # 新しくできる
        if (0 <= x-2) and (S[x-2], S[x-1]) == ("A", "B") and S[x] != "C" and c == "C":
            ans += 1
        if (0 <= x-1 and x+1 <= N-1) and (S[x-1], S[x+1]) == ("A", "C") and S[x] != "B" and c == "B":
            ans += 1
        if (x+2 <= N-1) and (S[x+1], S[x+2]) == ("B", "C") and S[x] != "A" and c == "A":
            ans += 1

        S[x] = c
        print(ans)

    return
######################################################

if __name__ == "__main__":
    main()
