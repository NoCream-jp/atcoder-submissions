"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < am i worth ARC?
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
    「0じゃないといけない桁」「1じゃないといけない桁」「そうじゃない桁」
    「そうじゃない桁」だらけだと考えられないのでナシ

    総当たりは2*10**4*100*2*100

    桁ごとに
    
    """

    N, M = i_map()
    l = [[0 for i in range(M)] for _ in range(N)]
    for n in l:
        print(n)
    S = [input() for _ in range(N)]
    S.sort()
    for s in S:
        print(s)


    return
######################################################

if __name__ == "__main__":
    main()
