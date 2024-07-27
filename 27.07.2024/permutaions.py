from itertools import permutations
inp=input().strip()
stri,k = inp.split()
k = int(k)
perm=permutations(sorted(stri),k)
for p in perm:
    print(''.join(p))
