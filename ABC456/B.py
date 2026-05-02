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

    A = i_list()
    B = i_list()
    C = i_list()
    v = 6**3
    count = 0
    for a in A:
        for b in B:
            for c in C:
                if set([a, b, c]) == set([4, 5, 6]):
                    count += 1
    
    print(count / v)

    return
######################################################

if __name__ == "__main__":
    main()
