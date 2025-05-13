for A in range(1000, 1, -1):
    if all((A < 50) and ((x % A != 0) <= ((x % 10 == 0) <= (x % 12 != 0))) for x in range(1, 100)):
        print(A)
        break
