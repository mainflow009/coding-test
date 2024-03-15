S = input()
res = []


for i in range(len(S)):
    text = ""
    for j in range(i,len(S)):
        text += S[j]
        res.append(text)
 
res = set(res)
print(len(res))