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
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations as p

##################################################
def mex(a: int, b: int, c: int) -> int:
    for i in range(4):
        if i not in (a, b, c):
            return i
    return 3

def main():
    """
    それぞれのMより右にEとXが何個あって値が何かを探す
    今のMの値を固定したら、EとXのパターンは9個しかない。
    """

    N = int(input())
    A = i_list()
    S = input()

    l: dict[str, list] = {
        "E": [[0, 0, 0] for _ in range(N)],
        "X": [[0, 0, 0] for _ in range(N)],
    }
    l["EX"] = [[[0, 0, 0] for _ in range(3)] for _ in range(N)]

    i = N-1
    while 0 <= i:
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
                    
        for enum in range(3):
            for xnum in range(3):
                l["EX"][i][enum][xnum] = l["EX"][i+1][enum][xnum]
                
        if k == "E":
            enum = A[i]
            for xnum in range(3):
                l["EX"][i][enum][xnum] += l["X"][i+1][xnum]

    ans = 0
    for i in range(N-1):
        if S[i] != "M":
            continue
        mnum = A[i]
        for enum in range(3):
            for xnum in range(3):
                count = l["EX"][i+1][enum][xnum]
                
                if count > 0:
                    ans += mex(mnum, enum, xnum) * count
                    # print(f"mnum={mnum}, enum={enum}, xnum={xnum}, mex={mex(mnum, enum, xnum)}, count={count}, ans={ans}")
                    
    print(ans)

if __name__ == '__main__':
    main()
