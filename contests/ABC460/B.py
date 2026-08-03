"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < give me higher rate point !!!!
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
from itertools import permutations

##################################################

def get_dist(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

def main():
    T = int(input())

    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = i_map()
        d2 = get_dist(x1, y1, x2, y2)
        ans = "None"
        
        if d2 == 0 and r1 == r2:
            ans = "Yes"
        elif (r1 + r2) ** 2 < d2:
            ans = "No"
        elif (r1 + r2) ** 2 == d2:
            ans = "Yes"
        elif (r1 - r2) ** 2 < d2 < (r1 + r2) ** 2:
            ans = "Yes"
        elif d2 == (r1 - r2) ** 2:
            ans = "Yes"
        else:
            ans = "No"
            
        print(ans)




    return
######################################################

if __name__ == "__main__":
    main()
