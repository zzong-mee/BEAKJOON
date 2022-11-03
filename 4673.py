ntrNum = set(range(1,10001))
genNum = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    genNum.add(i)

selfNum = sorted(ntrNum - genNum)
for i in selfNum:
    print(i)




