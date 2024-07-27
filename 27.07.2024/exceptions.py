n=int(input())
for _ in range(n):
    try:
        a,b=input().split()
        a=int(a)
        b=int(b)
        res=a//b
        print(res)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
