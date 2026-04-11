###################################################
# 入力
# sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# alpha = "abcdefghijklmnopqrstuvwxyz"
# MOD = 998244353
drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


def c_list():
    return list(input().split())


# from collections import defaultdict
# from sortedcontainers import SortedList
# from collections import deque
# import heapq
# import math
# import bisect

# from itertools import permutations as p

##################################################


def main():
    """
    交差パターンと入れ違いパターンと追従パターン
    斜め無しと同時に動くことから追従が不可能なときもある
    同じマスに到達したらおなじ方向にいかないかチェックしたい
    """
    Rt, Ct, Ra, Ca = i_map()
    N, M, L = i_map()
    tlist = [list(input().split()) for _ in range(M)]
    alist = [list(input().split()) for _ in range(L)]

    # 問題文の座標系に合わせた移動方向の定義
    # U: 上 (-1, 0), D: 下 (1, 0), L: 左 (0, -1), R: (0, 1)
    move = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    # 相対座標で考える
    dr, dc = Ra - Rt, Ca - Ct
    answer = 0

    t_idx, a_idx = 0, 0
    t_rem, a_rem = 0, 0

    current_step = 0

    while True:
        if current_step >= N:
            break

        if t_rem == 0:
            if t_idx < M:
                drctt, dt_str = tlist[t_idx]
                t_rem = int(dt_str)
                t_idx += 1
            else:
                drctt = ""
                t_rem = float("inf")

        if a_rem == 0:
            if a_idx < L:
                drcta, da_str = alist[a_idx]
                a_rem = int(da_str)
                a_idx += 1
            else:
                drcta = ""
                a_rem = float("inf")

        # 共通の移動ステップ数を決定
        step = min(t_rem, a_rem, N - current_step)

        # 移動方向を決定
        dr_t, dc_t = move.get(drctt, (0, 0))
        dr_a, dc_a = move.get(drcta, (0, 0))

        # 単位時間あたりの相対位置の変化量
        dr_rel = dr_a - dr_t
        dc_rel = dc_a - dc_t

        # 判定ロジック
        if dr == 0 and dc == 0:
            # 現在同じマスにいる場合
            if dr_rel == 0 and dc_rel == 0:
                answer += step
            else:
                answer += 1
        else:
            # 現在異なるマスにいる場合
            # dr + k * dr_rel == 0 and dc + k * dc_rel == 0 となる 0 < k <= step を探す
            k = float("inf")

            if dr_rel != 0 and dr % dr_rel == 0:
                k_r = -dr // dr_rel
                if k_r > 0:
                    k = k_r

            if dc_rel != 0 and dc % dc_rel == 0:
                k_c = -dc // dc_rel
                if k_c > 0:
                    if k == float("inf") or k_c < k:
                        k = k_c

            # x, y 両方で交差条件を満たすかチェック
            if dr_rel != 0 and dc_rel != 0:
                k_r = -dr // dr_rel
                k_c = -dc // dc_rel
                if dr % dr_rel == 0 and dc % dc_rel == 0 and k_r == k_c and k_r > 0:
                    k = k_r
                else:
                    k = float("inf")

            if k != float("inf") and 0 < k <= step:
                answer += 1

        # 相対位置を更新
        dr += dr_rel * step
        dc += dc_rel * step

        # 残りのステップ数を更新
        t_rem -= step
        a_rem -= step
        current_step += step

    print(answer)


#########################################################################

if __name__ == "__main__":
    main()
