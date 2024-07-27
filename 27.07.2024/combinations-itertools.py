from itertools import combinations
def combi():
    inp=input().strip()
    stri,size=inp.split()
    size = int(size)
    sort=''.join(sorted(stri))
    for si in range(1,size + 1):
        for combo in combinations(sort,si):
            print(''.join(combo))
combi()
