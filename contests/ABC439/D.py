"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗
                    ████╝ green tea

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

# from sortedcontainers import SortedList
# from collections import deque
import heapq

# import math
import bisect

from itertools import permutations as p

##################################################


def main():
    """
    RLEをソートして3:5になれば7もさがす、なければ打ち切り
    を全部についてやりたい、できそう

    ソートしたら添え字がわからなくなるので、
    RLEソートして数えるだけ数えて、
    ngなものを初めの配列見て引いていくことをしたい

    9使えるってわかってから9,15,21のもとのインデックスを見に行って、
    ngな組み合わせを省くのにはO(N)しかかからないとおもう

    9, 15, 21なら
    15の添え字が必ずjになるので、15の添え字5, 17全部についてそれより小さい
    、大きいをすべて数えたい
    時間かかりそうなので辞書の中でにぶたんする。
    15の添え字より小さい奴が9と21の添え字の中で何個ずつあるか

    ・初めにset化して、真ん中からみて3/5と7/5になるやつがあるかどうか
    見ておく。
    ・あったやつだけについて、辞書のなかでにぶたん使いながら探す。
    """
    N = int(input())
    A = i_list()

    st = set(A)

    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]].append(i)
        else:
            d[A[i]] = [i]
    # print(d)

    L = []
    for i in range(len(A)):
        if (A[i] * 3 / 5 in st) and (A[i] * 7 / 5 in st):
            L.append(A[i])

    setL = list(set(L))

    ans = 0
    for five in setL:  # 扱うべきやつらだけ
        for five_idx in d[five]:
            three = five * 3 / 5
            seven = five * 7 / 5
            lowcount, highcount = 0, 0
            # まずj(five)以下なのがlow, highについて何個あるか
            three_lc = bisect.bisect_right(d[three], five_idx)
            seven_lc = bisect.bisect_right(d[seven], five_idx)
            lowcount = three_lc * seven_lc
            # 次にj(mid)より大きい（以上）のが何個あるか
            three_hc = len(d[three]) - bisect.bisect_left(d[three], five_idx)
            seven_hc = len(d[seven]) - bisect.bisect_left(d[seven], five_idx)
            highcount = three_hc * seven_hc

            # print(f"five={five}, lowcount({d[three]}と{d[seven]}で{five_idx}を探索)\n\
            # ={three_lc}*{seven_lc}*={lowcount}, highcount={highcount}")
            ans += lowcount + highcount
            # print(f"five_idxについてのans={lowcount + highcount}")
    print(ans)

    return


######################################################


def rle(s):
    n = len(s)  # 文字列の長さ
    ans = []  # 圧縮後のリスト
    l = 0  # 始点
    while l < n:
        r = l + 1
        while r < n and s[l] == s[r]:  # 異なる文字になるまで進む
            r += 1
        ans.append((s[l], r - l))  # 文字,連続する個数
        l = r  # 連続しなかった文字から探索を開始
    return ans


if __name__ == "__main__":
    main()
