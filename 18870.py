n = int(input())
cdns = list(input().split())
cdn = list(set(map(int, cdns)))
cdn.sort()
dick = {}
for order, num in enumerate(cdn):
    dick[num] = order

for i in cdns:
    print(dick.get(int(i)), end=' ')