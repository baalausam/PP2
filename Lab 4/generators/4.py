def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


a = int(input("Enter a: "))
b = int(input("Enter b: "))
gen = squares(a, b)
for square in gen:
    print(square)