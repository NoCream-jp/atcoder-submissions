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
    S = input()
    a, b = S[0], S[-1]
    if S[-1] == "8":
        b = "1"
        a = str(int(a) + 1)
    else:
        b = str(int(b) + 1)
    print(f"{a}-{b}")


######################################################

if __name__ == "__main__":
    main()
