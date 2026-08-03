"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < give me higher rate point !!!!
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
# nを割り切る最大の平方数を返す
def solve(n):
    if n <= 1:
        return n
    for i in range(2, int(n**0.5) + 1):
        if n < i*i:
            break
        while n % (i*i) == 0:
            n //= (i*i)
    return n

def main():

    N = int(input())
    A = i_list()

    l = []
    zero = 0
    for a in A:
        if a == 0:
            zero += 1
        else:
            l.append(solve(a))

    ans = 0
    # 先に0を数える
    if zero:
        ans += zero*(zero-1)//2
        ans += zero*(N-zero)
    
    counts = Counter(l)
    for count in counts.values():
        if 2 <= count:
            ans += (count * (count - 1)) // 2
    print(ans)
    return
######################################################

if __name__ == "__main__":
    main()
