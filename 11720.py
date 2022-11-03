n1 = int(input())
n2 = input()
nList = []
for i in range(n1):
    nList.append(int(n2[i:i+1]))
print(sum(nList))