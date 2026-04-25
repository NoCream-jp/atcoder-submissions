"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < my cat running
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
def make_dictionary(lst):
    d = {}
    for n in lst:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    return d

def main():

    N, K = i_map()
    A = i_list()
    A.sort()

    if N == 1:
        print(0)
        return

    l = []
    tmp = A[0]
    count = 1
    for i in range(1, N):
        if tmp != A[i]:
            l.append(A[i-1] * count)
            count = 1
        else:
            count += 1

        tmp = A[i]
    l.append(A[i] *  count)
    l.sort()
    while K and l:
        l.pop()
        K -= 1
    
    print(sum(l))
    return
######################################################

if __name__ == "__main__":
    main()
