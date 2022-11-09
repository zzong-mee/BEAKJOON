n = int(input())
word = list(set([input() for _ in range(n)]))

word.sort() # 사전순
word = sorted(word, key = lambda s: len(s)) # 길이순

for i in word:
    print(i)