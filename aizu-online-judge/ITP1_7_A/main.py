while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break

    sum = m + f
    if m == -1 or f == -1:
        print('F')
    elif sum >= 80:
        print('A')
    elif sum >=65:
        print('B')
    elif sum >= 50 or r >= 50:
        print('C')
    elif sum >= 30:
        print('D')
    else:
        print('F')
