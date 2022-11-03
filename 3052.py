num = []
for i in range(10):
    num.append(int(input()))

rst = []
for i in range(10):
    rst.append(num[i] % 42)

count = 0
for i in range(42):
    if rst.count(i) >= 1:
        count += 1
    else:
        continue

print(count)





