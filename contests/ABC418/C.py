"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗   < ABC 418
                    ████╝

"""

import bisect as bs


# 入力
def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


def c_list():
    return list(input().split())


######################################################


def main():
    N, Q = i_map()
    A = i_list()

    """
    鳩ノ巣っぽいね
    bこのフラッシュを作らないといけない
    b個もらえるのは，ディーラーにフラッシュができないカードたち
    全部をもらってから．
    -1になるのはmax(A)がbより小さい場合．

    bって言われたらディーラーの最善は
    bに満たないものを全部渡してからb以上のカードを1枚ずつ渡していく

    求める答えは(枚数がb以下のカードの総和) + (b以上のカードの種類数(b枚以上なので全部ちまちま渡せる))*(b-1) + 1

    枚数ごとに管理するのがめんどい
    ソートして累積和
    """
    # cards = [[i, A[i]] for i in range(N)]
    # cards.sort(key = lambda x: x[1]) # 枚数でソート

    A.sort()

    # 累積和
    cum_sum = [0] * (N + 1)
    for i in range(N):
        cum_sum[i + 1] = cum_sum[i] + A[i]
    # 二重にする必要なし

    mx = max(A)
    sm = sum(A)

    # 左にぶたんでidx求めたら累積和から総和を引っ張れる
    for j in range(Q):
        b = int(input())
        if mx < b:
            print(-1)
            continue
        idx = bs.bisect_right(A, b - 1)
        # print(f"見つけたidx={idx}")

        # print(f"A:{A}からb-1={b-1}を探す")
        # print(f"idx = {idx}")
        # print(f"左側：{cum_sum[idx]}")
        # print(f"右側：{(N - idx) * (b-1)}, N={N}, idx={idx}, b-1={b-1}")
        ans = cum_sum[idx] + ((N - idx) * (b - 1)) + 1
        print(min(sm, ans))
        # print()


######################################################

if __name__ == "__main__":
    main()
