"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < playing
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

    while 1:
        n, m = i_map()
        if n == m == 0:
            return
        a = i_list()
        b = i_list()

        goal = [-1 for _ in range(n)]
        for i in range(n):
            goal[i] = (b[i] - a[i])%m

        # 最小の差分回は最低でも回す．
        # そこからはそれぞれの山の頂上までのぶん
        goal2 = []
        for i in range(n-1):
            goal2.append(goal[i+1] - goal[i])
        print(goal)
        print(goal2)
        # 差分が+から-に切り替わったとこが山
        top_index = -1
        ans = min(goal)
        for i in range(n-1-1):
            if 0 < goal2[i] and goal2[i+1] < 0 : # 頂点を通過
                top_index = i
            if goal2[i] < 0 and 0 < goal2[i+1]: # 谷を通過
                top_index = max()


    return
######################################################

if __name__ == "__main__":
    main()
