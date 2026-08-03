"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < hot
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

    T = input()
    N = int(input())
    l = [list(input().split()) for _ in range(N)]

    """
    temp[i] = i文字目までを完成させるのに何円かかったか
    """
    
    temp = [float('inf') for _ in range(len(T))]

    for i in range(N):
        for j in range(1, int(l[i][0])+1):
            string = l[i][j]
            for jj in range(len(T) - len(string)+1):
                # print(f"{T[jj:jj+len(string)]}")
                if T[jj:jj+len(string)] == string:
                    if i == 0:
                        temp[jj+len(string)-1] = 1
                    else:
                        temp[jj+len(string)-1] = min(temp[jj+len(string)-1], temp[jj-1] + 1)
            # print(temp)
    print(temp[-1])
    

    return
######################################################

if __name__ == "__main__":
    main()