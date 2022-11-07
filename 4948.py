def decimal(x):
    if x == 1:
        return False
        
    for k in range(2, int(x**0.5)+1):
        if x % k == 0:
            return False

    return True

decimal_nums = []
for i in range(2, 246912):
    if decimal(i):
        decimal_nums.append(i)

while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break

    for j in decimal_nums:
        if n < j <= 2 * n:
            cnt += 1

    print(cnt)