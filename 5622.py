num = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
word = list(input())
result = 0
for i in word:
    for j in num:
        if i in j:
            result += num.index(j) + 3     
print(result)








