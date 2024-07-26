def cap(name):
    w=name.split()
    cap_w = [wo.capitalize() for word in words]
    cap_name = ' '.join(cap_w)
    return cap_n
if __name__ == '__main__':
    name = input().strip()
    res = cap(name)
    print(res)
