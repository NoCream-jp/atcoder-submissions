"""
Here is my coding space
Caffeineholic
) ) )
( ( (
████╗
████╝ < chill

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


# from collections import defaultdict
# from sortedcontainers import SortedList
# from collections import deque
# import heapq
# import math
# import bisect
# from itertools import permutations as p

##################################################


def main():
    n, r = i_map()
    r -= 1
    l = i_list()

    """
    引き返す地点を探す．
    端から1が続くようならそこへは行かなくてよい.
    """

    if sum(l) == n or sum(l) == 0:
        print(0)
        return

    le, ri = 0, n - 1
    while l[le] == 0 and le < n - 1:
        le += 1
    while l[ri] == 0 and ri > 0:
        ri -= 1

    cost1 = (r - le) + (ri - le) + sum(l)
    cost2 = (ri - r) + (ri - le) + sum(l)

    print(min(cost1, cost2))


######################################################

if __name__ == "__main__":
    main()
