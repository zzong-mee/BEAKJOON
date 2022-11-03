n = int(input())
grade = list(map(int, input().split()))
print(round((sum(grade)/n)/max(grade)*100, 2))