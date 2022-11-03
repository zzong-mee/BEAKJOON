c = int(input())
for i in range(c):
    strn = list(map(int, input().split()))
    n = strn[0]
    del strn[0]
    avg = sum(strn)/n
    count = 0
    for i in range(len(strn)):
        if strn[i] > avg:
            count += 1
        else:
            continue
    print(format((count/len(strn))*100, ".3f")+"%")
