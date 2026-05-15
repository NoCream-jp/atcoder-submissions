"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < try to solve light blue prob
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

    """
    各警備員からBFSは間に合わない

    各頂点に到達できる警備員の体力の最大値を確定させてゆく
    優先度付きキューで一番強い警備員を選んで、
    そいつより大きくなることはあり得ないのでそいつがいる場所を確定させる
    そいつの周り全部についてキューに入れる。確定済みならとばす
    繰り返してキューに何もなければ終わり
    """
    N, M, K = i_map()
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = i_map()
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    q = []
    heapq.heapify(q)
    # 確定済みした頂点たち
    # iに到達できる警備員の最大の体力を格納
    ans = [-1 for _ in range(N)]
    for _ in range(K):
        p, h = i_map()
        p -= 1
        ans[p] = h
        heapq.heappush(q, (-h, p))
    
    while q:
        h, p = heapq.heappop(q)
        h *= -1
        # セット使わなくてもこれでよい
        if ans[p] != h:
            continue
        # 体力マイナスは入れられない
        if h == 0:
            continue

        for neighbor in graph[p]:
            # 更新する価値のある場合（すでにある値よりhが大きい）のみ更新する
            if ans[neighbor] < h-1:
                ans[neighbor] = h-1
                heapq.heappush(q, (-(h-1), neighbor))
    
    output = []
    for i in range(N):
        if 0 <= ans[i]:
            output.append(i+1)
    print(len(output))
    print(*output)

    return
######################################################

if __name__ == "__main__":
    main()
