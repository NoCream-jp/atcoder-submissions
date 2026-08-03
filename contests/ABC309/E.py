"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < green
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
    昇順だということに気づかなかった。人2が人7の子だということはあり得ないので、
    昇順に何代後まで続くかをメモしていくだけで大丈夫
    """

    N, M = i_map()
    P = i_list()

    # 人iが最大で何代後まで補償を持っているか
    memo = [-1 for _ in range(N)]
    for _ in range(M):
        x, y = i_map()
        x -= 1
        memo[x] = max(memo[x], y)
    # print(memo)

    for i in range(1, N):
        parent = P[i-1] - 1
        memo[i] = max(memo[parent]-1, memo[i])
    # print(memo)

    count = 0
    for i in range(N):
        if 0 <= memo[i]:
            count += 1
    print(count)



    
    
    return
######################################################

if __name__ == "__main__":
    main()
