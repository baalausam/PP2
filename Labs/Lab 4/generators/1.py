def squares(N):
    for i in range(N+1):
        yield i ** 2


N = int(input("Enter the value of N: "))
gen = squares(N)
for square in gen:
    print(square)
    
    
    
