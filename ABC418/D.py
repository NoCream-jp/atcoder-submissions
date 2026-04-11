"""
Here is my coding space
    Caffeineholic
                    ) ) )
                    ( ( (
                    ████╗   < ABC 418
                    ████╝

"""


# 入力


def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


def c_list():
    return list(input().split())


######################################################


def main():
    """
    累積XORしたい
    累積xorが1なら0になるし0なら1になる？

    累積xorの累積和を取ったら，桁追加した時に全部含めた反転回数？
    みたいなの数えられる？
    """
    N = int(input())
    T = input()
    l = [1 - int(T[i]) for i in range(N)]

    cum_sum = [0] * (N + 1)
    for i in range(N):
        cum_sum[i + 1] = cum_sum[i] ^ l[i]

    print(cum_sum)


######################################################

if __name__ == "__main__":
    main()
