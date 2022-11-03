s = list(input())
apb_list = [chr(i) for i in range(ord('a'),ord('z')+1)]
ans = [-1]*(len(apb_list))

for i in range(len(apb_list)):
    if apb_list[i] in s:
        ans[i] = s.index(apb_list[i])

print(*ans, sep=' ')












