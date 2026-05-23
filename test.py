import bisect as bs

l = [1, 3]
idx = bs.bisect_left(l, 2)
print(idx)