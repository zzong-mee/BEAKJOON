num = [int(input()) for i in range(10)]
rst = [num[i]%42 for i in range(10)]
count = 0
for i in range(42):
    if rst.count(i) >= 1:
        count += 1
    else:
        continue
print(count)
