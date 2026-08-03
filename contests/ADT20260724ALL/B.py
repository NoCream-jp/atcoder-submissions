N = int(input())
H = list(map(int, input().split()))
A = [(H[i], i) for i in range(N)]
A.sort()
print(A[-1][-1] + 1)
