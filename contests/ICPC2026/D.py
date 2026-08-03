###################################################
# alpha = "abcdefghijklmnopqrstuvwxyz"
# MOD = 998244353
# drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


def c_list():
    return list(input().split())


##################################################


def main():

    aa = []

    while 1:
        s, k = i_map()
        if s == k == 0:
            break
        if k == 1:
            aa.append(s)
            continue
        if (s * s + 1 <= k):
            if (s * s + 1 == k):
                aa.append(s)
                continue
            ans = 0
            right = 0
            left = 1
            for i in range(s -1, -1, -1):
                right = left + 2 * i + 1
                num = s - i
                if right == k:
                    ans = s
                    break
                index = k - left
                if right > k:
                    if num % 2 == 0:
                        ans = num
                    else:
                        ans = num + index // 2
                    break
                left = right
            aa.append(ans)
            continue
        else:
            i = 0
            right = 0
            left = s * s + 1
            while True:
                i += 1
                right = left + 2 * (s + i)
                if right >= k:
                    num = s + i
                    index = k - left
                    if num % 2 == 0:
                        ans = index // 2
                    else:
                        ans = num
                    break
                left = right
            aa.append(ans)

    for a in aa:
        print(a)
            


######################################################

if __name__ == "__main__":
    main()