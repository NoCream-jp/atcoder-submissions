"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < 42222222

"""

###################################################
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
    """
    a < c -> min(a, b+(c-a))  少ない方しか開催できない．aが少なければa回またはb+余ったc回
    c < a -> min(c, b+(a-c))
    """

    T = int(input())
    count = 0
    for t in range(T):
        a, b, c = i_map()
        count = min(a, b, c)
        a -= count
        c -= count
        tmp = min(a, c, (a + c) // 3)
        print(count + tmp)


######################################################

if __name__ == "__main__":
    main()
