def fib(n):
    if n<= 0:
        return "Invalid input. Please enter a positive integer."
    seq=[0, 1]
    for i in range(2, n):
        ne=seq[-1]+seq[-2]
        seq.append(ne)
    return seq[:n] 

n=int(input("Enter the number of terms: "))
res=fib(n)
print(res)
