n = int(input("Enter a number: "))

if n%2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")

if n> 1:
    for i in range(2, int(n**0.5)+1):
        if n % 1 == 0:
            print(f"{n} is not a Prime")
            break
    else:
        print(f"{n} is Prime")
else:
    print(f"{n} is not a Prime")