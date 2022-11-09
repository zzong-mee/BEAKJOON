n = int(input())

cdn = []
for _ in range(n):
    cdn.append(list(map(int, input().split())))
    
cdn.sort()
cdn = sorted(cdn, key=lambda x: x[1])
for i in range(n):
    print(cdn[i][0], cdn[i][1])















