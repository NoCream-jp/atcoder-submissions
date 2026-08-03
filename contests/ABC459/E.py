"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ < give me money?
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
def EulerTour(n, X, i0):
    done = [0] * n
    Q = [~i0, i0] # 根をスタックに追加
    ET = []
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            ET.append(i)
            for a in X[i][::-1]:
                if done[a]: continue
                Q.append(~a) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加
        
        else: # 帰りがけの処理
            ET.append(~i)
    
    return ET


def main():

    """
    iを根とする部分木上に存在する飴の数はわかる
    不可能な時っていうのはあるアメ以上にリスの要求が多いとき

    可能として考える。
    ・iを根とする部分木は1パターンで、その上にあるアメ
    を数えておく必要がある
    全部のノードから、親に遡及することは難しくないと思ったけど
    それはトポロジカルソートされてるときだけで今回はわからない
    ●できたらいいアルゴリズム：
    木において全ての頂点が、自分が根になっている部分木全体のコストの総和を持っている
    状態にする
    ・リス毎にまとめて置いたらほしいアメの数がわかるから
    言われている部分木ごとにアメCリスを計算するだけ
    """

    N = int(input())
    P = i_list()
    C, D = i_list(), i_list()

    graph = [[] for _ in range(N)]
    for i in range(N-1):
        node = i+1 # P[i-1]とi+1が親子
        graph[node].append(P[i]-1)
        graph[P[i]-1].append(node)

    l = EulerTour(N, graph, 0) # 部分木ごとの子のこすとの総和

    # コスト書き込み
    for i in range(N):
        for j in range(len(graph[i])):
            graph[i][j] = (graph[i][j], C[i])

    print(graph)

    # 木上にスコアを配置するってのはライブラリ持ってたほうがいいかも
    # 配置も部分木についての取得も
    


    return
######################################################

if __name__ == "__main__":
    main()
