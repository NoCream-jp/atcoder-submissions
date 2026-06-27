"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < too hot
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
    被った色をどうするか
    辞書もっていもす
    """

    N, M = i_map()

    l = [[[], []] for _ in range(M)] # inリストとoutリスト
    dict = defaultdict(int)
    for i in range(N):
        a, d, b = i_map()
        l[0][0].append(a)
        l[d-1][1].append(a)
        l[d-1][0].append(b)
    
    # print(l)
    ans = 0
    for i in range(M):
        while l[i][0]:
            t = l[i][0].pop()
            dict[t] += 1
            if dict[t] == 1:
                ans += 1
        while l[i][1]:
            t = l[i][1].pop()
            dict[t] -= 1
            if dict[t] == 0:
                ans -= 1
        # print(dict)
        print(ans)


    return
######################################################

if __name__ == "__main__":
    main()