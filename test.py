a = int(input("Zadejte celé číslo: "))
b = int(input("Zadejte celé číslo: "))
c = int(input("Zadejte celé číslo: "))

if (a > b) and (a > c) and (b > c):
    print(a, b, c)
elif (b > a) and (b > c) and (a > c):
    print(b, a, c)
elif (c > a) and (c > b) and (b > a):
    print(c, b, a)
elif (a > b) and (a > c) and (c > b):
    print(a, c, b)
elif (c > b) and (c > a) and (a > b):
    print(c, a, b)