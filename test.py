s = list(input())

head = 0
index = 1
result = 0
end = False

# print(len(s))

# 長さ1
if len(s) == 1:
  result = 1
# それ以外
else:
  while True:
    # 終了フラグが立っている時
    if end == True:
      break
    # 端まで見た時
    elif index == len(s) - 1:
      result += (index - head + 2) * (index - head + 1) // 2
      break
    # 部分文字列の左端を見つけた時
    elif s[index] == s[index + 1]:
      print(f"{index}|{index+1}で切る")
      print(f"{index}と{head}で計算")
      result += (index - head + 2) * (index - head + 1) // 2
      # 部分文字列の右端を見つけて次のheadにする
      k = 1
      while True:
        # 端まで見つからなかったら終わり
        if index + k >= len(s):
          print("端まで見つからなかったので終わり")
          end = True
          break
        # 端を見つけたらheadとindexを更新
        elif s[index] != s[index + k]:
          head = index + k - 1
          index = head + 1
          print(f"端を見つけたのでhead={head}, index={index}")
          break
        else:
          k += 1
    else:
      print(f"index+=1で進める")
      index += 1

print(result)