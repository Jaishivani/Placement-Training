def eva(n):
    if n % 2 != 0:
        print("Good")
    elif n % 2 == 0:
        if 2 <= n <= 5:
            print("Not Good")
        elif 6 <= n <= 20:
            print("Good")
        elif n > 20:
            print("Not Good")

# Main block to execute the program
if __name__ == '__main__':
    n = int(input().strip())
    eva(n)
