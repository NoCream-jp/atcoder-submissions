def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


def c_list():
    return list(input().split())


N, W = i_map()

Weight, Value = [0 for _ in range(N)], [0 for _ in range(N)]
for i in range(N):
    Weight[i], Value[i] = i_map()

dp = [[0 for i in range(W)] for j in range(N + 1)]
