"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < tired
"""
###################################################

# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
MOD = 998244353
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

def calc(n):
    return (n**2 + n) // 2


def main():

    """
    同じ文字がある場所で区切ってできる文字列のパターンを足せばいい
    3つ以上ある場合はどうするか

    baaabbaなら
    ba, a, ab, baにわけて3, 1, 3, 3の和で10
    """
    S = input()
    count = 1
    lst = [] ## 何個ずつに分かれるか
    for i in range(len(S) - 1):
        if S[i] == S[i+1]:
            lst.append(count)
            count = 1
        else:
            count += 1
    lst.append(count)

    ans = 0
    for num in lst:
        ans = (ans + calc(num)) % MOD
    print(ans)

    return
######################################################

if __name__ == "__main__":
    main()
