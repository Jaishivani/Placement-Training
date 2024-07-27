def wrap(stri,wid):
    lin= []
    for i in range(0, len(stri),wid):
        lin.append(stri[i:i+wid])
    return '\n'.join(lin)
stri=input()
wid=int(input())
res=wrap(stri,wid)
print(res)
