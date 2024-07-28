def get_input(a="Enter an integer:"):
    while True:
        input=a(int)
        try:
            value=int(input)
            return value
        except ValueError:
            print("invalid integer")
integer=get_input()
print(f"you entered{integer}")
