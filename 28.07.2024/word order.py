n=int(input())
wo={}
ord=[]
for _ in range(n):
    word=input().strip()  
    if word in wo:
        wo[word]+=1 
    else:
        wo[word]=1 
        ord.append(word)  
print(len(ord))
print(" ".join(str(wo[word]) for word in ord))
