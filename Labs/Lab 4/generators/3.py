def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = int(input("Enter the value of n: "))
gen = divisible(n)
for number in gen:
    print(number)