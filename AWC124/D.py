N, K = map(int, input().split())
l = [map(int, input().split()) for i in range(N)]

wsum, ssum = 0, 0
for w, s in l:
    wsum += w
    ssum += s

print(ssum if K <= wsum else -1)