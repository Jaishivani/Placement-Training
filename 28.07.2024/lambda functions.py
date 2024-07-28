cube=lambdax:x**3
def fib(n):
    fib_li=[0, 1]
    while len(fib_li)<n:
        fib_li.append(fib_li[-1]+fib_li[-2])
    return fib_li[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fib(n))))
