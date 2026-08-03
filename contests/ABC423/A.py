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
    X, C = i_map()

    a = X // 1000
    ans = 0
    for i in range(a):
        if i * 1000 + i * C <= X:
            ans = i * 1000
        else:
            break
    print(ans)


######################################################

if __name__ == "__main__":
    main()
