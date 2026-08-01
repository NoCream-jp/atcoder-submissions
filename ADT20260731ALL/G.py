_ = int(input())

l = [i for i in range(1, 101)]

ans = []

for i in range(3):
    for n in l:
        ans.append(n * 100**i)
print(len(ans)) 
print(*ans)
