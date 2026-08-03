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
    N = int(input())
    L = i_list()
    st = set()
    for i in range(len(L)):
        if not L[i]:
            st.add(i + 1)

    """
    ドアは1~N
    """
    visited = [False for _ in range(N + 1)]
    visited[0] = True
    visited[N] = True
    l = 0
    while l + 1 in st:
        l += 1
        visited[l] = True
    r = N
    while r in st:
        r -= 1
        visited[r] = True
    # print(st)
    # print(visited)
    print(N + 1 - sum(visited))


######################################################

if __name__ == "__main__":
    main()
