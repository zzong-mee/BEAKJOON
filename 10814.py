n = int(input())
users= list([input().split() for _ in range(n)])
users.sort(key = lambda age:int(age[0]))
for i in range(n):
    print(users[i][0], users[i][1])