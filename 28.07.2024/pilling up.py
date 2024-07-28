def can_stack_cubes(cub):
    l=0
    r=len(cub)-1
    l=float('inf')
    while l<=r:
        if cub[l]>=cub[r]:
            curr=cub[l]
            l+=1
        else:
            curr=cub[r]
            r-=1
        if curr>la:
            return "No"
        la=current 
    return "Yes"
def main():
    T=int(input())
    res=[]
    for _ in range(T):
        n=int(input())
        cub=list(map(int,input().split()))
        res=can_stack_cubes(cub)
        res.append(res)
    for r in res:
        print(r)
if __name__ == "__main__":
    main()
