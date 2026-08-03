"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < give me money?
"""
###################################################
# import sys
# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
alpha = "abcdefghijklmnopqrstuvwxyz"
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
from itertools import permutations

##################################################


def main():

    l = [
        [{"a", "b", "c"}, 2],
        [{"d", "e", "f"}, 3],
        [{"g", "h", "i"}, 4],
        [{"j", "k", "l"}, 5],
        [{"m", "n", "o"}, 6],
        [{"p", "q", "r", "s"}, 7],
        [{"t", "u", "v"}, 8],
        [{"w", "x", "y", "z"}, 9]
    ]

    N = int(input())
    S = list(input().split())
    ans = ""
    for s in S:
        for alpha in l:
            if s[0] in alpha[0]:
                ans += str(alpha[1])
                break
    print(ans)

    return
######################################################

if __name__ == "__main__":
    main()
