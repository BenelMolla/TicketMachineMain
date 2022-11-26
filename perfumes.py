def perfumery():
    a = 1
    b = 0
    while True:
        yield a
        a, b = a + 1, b + 1

    Ticket = perfumery()
    while True:
        customer = input("choose p for perfumery ")
        if customer == "c":
            print(next(Ticket))


perfume = perfumery()
