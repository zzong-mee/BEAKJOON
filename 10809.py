s = input() # apple
apb = [chr(i) for i in range(ord('a'),ord('z')+1)]
div_s = [s[i:i+1] for i in range(len(s))]
ans = []
c = 0
for i in range(len(apb)):
    if apb[i] in div_s:
        ans.append(apb.index(div_s[c]))
        c += 1
    
    else:
        ans.append(-1)

print(ans)













