"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < midnight coding
"""
###################################################
# import sys
# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
# MOD = 998244353
# drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
drct_char = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

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

    N = int(input())

    st = set()
    x, y = 0, 0
    st.add((x, y))
    for c in input():
        dx, dy = drct_char[c]
        x += dx
        y += dy
        if (x, y) in st:
            print("Yes")
            return
        st.add((x, y))
    print("No")

    return
######################################################

if __name__ == "__main__":
    main()