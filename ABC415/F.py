import bisect as bs


# 入力
def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


######################################################


def main():
    N, Q = i_map()
    A = i_list()

    # 枚数でソート
    A.sort()

    # 累積和を計算
    cum_sum = [0] * (N + 1)
    for i in range(N):
        cum_sum[i + 1] = cum_sum[i] + A[i]

    mx = A[-1]  # ソート済みなので最後の要素が最大
    sm = cum_sum[-1]  # 全カードの合計枚数

    for j in range(Q):
        b = int(input())

        if mx < b:
            print(-1)
            continue

        # 枚数がb-1以下のカードのインデックスを探す
        idx = bs.bisect_right(A, b - 1)

        # 枚数がb-1以下のカードの総和
        sum_less_than_b = cum_sum[idx]

        # 枚数がb以上のカードの種類数
        num_greater_than_b = N - idx

        # フラッシュに必要な要求枚数
        ans = sum_less_than_b + (num_greater_than_b * (b - 1)) + 1

        # 全カードの枚数と比較して小さい方を出力
        print(min(sm, ans))
        print()


######################################################

if __name__ == "__main__":
    main()
