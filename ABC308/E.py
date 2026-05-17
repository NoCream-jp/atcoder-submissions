"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < difficult 
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
from sys import breakpointhook
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations as p

##################################################
def mex(a, b, c):
    st = set([a, b, c])
    if len(st) == 3:
        return 3
    for n in range(3):
        if n not in st:
            return n
    return -1

def main():

    """
    それぞれのMより右にEとXが何個あって値が何かを探す
    今のMの値を固定したら、EとXのパターンは9個しかない。
    3行
    """

    N = int(input())
    A = i_list()
    S = input()

    l = {k: [[0, 0, 0] for _ in range(N)] for k in "EX"}
    i = N-1
    while 0 < i:
        if S[i] == "X":
            l["X"][i][A[i]] = 1
            break
        i -= 1
    for i in range(N-1)[::-1]:
        k = S[i]
        for c in "EX":
            for n in range(0, 3):
                if c == k and n == A[i]:
                    l[c][i][n] = l[c][i+1][n] + 1
                else:
                    l[c][i][n] = l[c][i+1][n]
    for k in l:
        for j in range(3):
            for i in range(N):
                print(l[k][i][j], end=" ")
            print()
        print()
    
    ans = 0
    for i in range(N-1):
        if S[i] != "M":
            continue
        mnum = A[i]
        for enum in range(3):
            for xnum in range(3):
                # 何回mex計算をするか
                count = l["E"][i+1][enum] * l["X"][i+1][xnum]
                ans += mex(mnum, enum, xnum) * count
                print(f"mnum={mnum}, enum={enum}, xnum={xnum}, mex={mex(mnum, enum, xnum)}, count={count}, ans={ans}")
    print(ans)

            
                    


    return
######################################################

if __name__ == "__main__":
    main()
