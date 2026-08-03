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
    クエリをソート
    """
    N = int(input())
    T = []
    for i in range(N):
        h, l = i_map()
        T.append((-h, l))
    heapq.heapify(T)
    
    Q = int(input())
    query = i_list()
    q = [(i, query[i]) for i in range(Q)]
    q.sort(key=lambda x: x[-1])

    ans = [-1 for _ in range(Q)]
    tidx = 0
    for i in range(Q):
        qidx, time = q[i]
        while T and T[tidx][1] <= time:
            heapq.heappop(T)
        if T:
            ans[qidx] = -T[0][0]
        else:
            ans[qidx] = 0
    
    for a in ans:
        print(a)

            
        
        


    return
######################################################

if __name__ == "__main__":
    main()
