"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗   <  421...
                    ████╝

"""

###################################################
# 入力
# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
# MOD = 998244353
drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


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
    N = int(input())
    S = list(input())

    """
    2通り試す 左からふさわしい場所に最近のAを持っていく
    ababとbaba
    aaabbb
    """

    copy = S[:]
    # AB
    l = None
    count = 0
    for i in range(2 * N):
        if i % 2 == 0 and copy[i] == "A":
            continue
        if i % 2 == 1 and copy[i] == "B":
            continue
    print(count)


#########################################################################

if __name__ == "__main__":
    main()
