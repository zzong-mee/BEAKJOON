n, m = map(int, input().split())
num = list(map(int, input().split()))
sum = 0
num.sort()

for i in num:
    if i > m:
        continue

    elif i == m:
        sum += i
        break

    else:
        if sum + i > m:
            continue

        else:
            sum += i

print(sum)