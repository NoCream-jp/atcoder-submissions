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
from sortedcontainers import SortedList
from collections import deque
import heapq
import math
import bisect
from itertools import permutations

##################################################
drct8 = drct8 = [
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1)   
]
def main():

    """
    ななめもりんせつ

    黒からいくつ離れているかで
    「何回目の操作から反転繰り返し始めるか」がわかるかも
    #....の端なら4離れているので4回目に黒になるので最後は黒
    全ますについてそれを求めたら答えわかる

    それは黒から探索で全マスだせるかも
    各黒からDFSして埋めていくのは効率悪すぎる
    BFSならOKか

    黒がありさえすれば間違ってないから、まったくないときだけ例外？

    間違ってた
    周りに黒がない白は二度と変わらないので黒がないケースと全部黒のケースをはじいたけど
    だめらしい

    かたまりで黒があるとその中で色がかわることがあるので
    黒ならこうなる ではない
    周りの白との距離でランクづけしたい

    一回だけ反転した後から見るのでは不十分　波及していくから

    実際に1000くらい回すのは考えたが、間に合わなさそう
    
    
    """

    H, W = i_map()
    grid = [list(input()) for _ in range(H)]

    # はじめに黒
    q = deque()
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#":
                q.append((i, j, 0))

    # 黒ない場合
    if not q or len(q) == H*W:
        for i in range(H):
            for j in range(W):
                print(".", end="")
            print()
        return

    visited = [[-1 for _ in range(W)] for _ in range(H)]
    while q:
        i, j, stamp = q.popleft()
        if visited[i][j] != -1:
            continue
        visited[i][j] = stamp
        for di, dj in drct8:
            ni, nj = i+di, j+dj
            if 0 <= ni <= H-1 and 0 <= nj <= W-1:
                if visited[ni][nj] == -1:
                    q.append((ni, nj, stamp+1))
    # for v in visited:
    #     print(v)

    for i in range(H):
        for j in range(W):
            if visited[i][j] % 2 == 0:
                grid[i][j] = "#"
            else:
                grid[i][j] = "."
    
    for i in range(H):
        for j in range(W):
            print(grid[i][j], end="")
        print()



    return
######################################################

if __name__ == "__main__":
    main()
