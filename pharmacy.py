def Pharmaceuticals():
    a = 1
    b = 0
    while True:
        yield a
        a, b = a + 1, b + 1

    z = Pharmaceuticals()
    while True:
        customer = input("choose ph for Pharmaceuticals ")
        if customer == "c":
            print(next(z))


pharmacy = Pharmaceuticals()
