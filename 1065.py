n = int(input())

hs = 0
for i in range(1, n+1):
    nList = list(map(int, str(i)))

    if i < 100:
        hs += 1

    elif nList[0] - nList[1] == nList[1] - nList[2]:
        hs += 1

print(hs)






