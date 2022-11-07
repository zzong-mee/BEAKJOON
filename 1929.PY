m, n = map(int, input().split())
prime = []

for i in range(m, n+1):
    cnt = 0
    if i > 1 :
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
                break

        if cnt == 0 :
            prime.append(i)
            
for i in prime:
    print(i)