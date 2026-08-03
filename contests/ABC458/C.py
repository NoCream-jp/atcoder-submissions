"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < difficult?
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
from re import I
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations as p

##################################################


def main():

    S = input()
    """
    Cの位置と数だけ見ればいい
    Cを見つけるたびに答えに（右と左にある文字数の少ないほう）+1個足す
    """
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] == "C":
            left, right = i, N-1-i
            ans += min(left, right) + 1
    print(ans)


    return
######################################################

if __name__ == "__main__":
    main()
