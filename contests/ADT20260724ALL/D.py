a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = 0
# 456
ans += a.count(4) * b.count(5) * c.count(6) / 216
# 465
ans += a.count(4) * b.count(6) * c.count(5) / 216
# 546
ans += a.count(5) * b.count(4) * c.count(6) / 216
# 564
ans += a.count(5) * b.count(6) * c.count(4) / 216
# 645
ans += a.count(6) * b.count(4) * c.count(5) / 216
# 654
ans += a.count(6) * b.count(5) * c.count(4) / 216
print(ans)