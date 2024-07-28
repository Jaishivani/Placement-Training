a=int(input())
b=int(input())
for n in range(a,b+1):
    sum=0
    order=len(str(a))
    temp=n
    while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp=temp//10
    if n==sum:
        print(n)
