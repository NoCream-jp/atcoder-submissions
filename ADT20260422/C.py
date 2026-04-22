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
    
    s = list(input())
    N = len(s)
    c = 0
    if s[0] == "o":
        c += 1
    for i in range(N-1):
        if s[i] == s[i+1]:
            c += 1
    if (N+c)%2 == 1:
        c += 1
    print(c)


    return
######################################################

if __name__ == "__main__":
    main()
