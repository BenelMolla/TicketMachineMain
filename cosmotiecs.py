def cosmotics():
    a = 1
    b = 0
    while True:
        yield a
        a, b = a + 1, b + 1

    z = cosmotics()
    while True:
        customer = input("choose c for cosmetics ")
        if customer == "c":
            print(next(z))


cosmo = cosmotics()
