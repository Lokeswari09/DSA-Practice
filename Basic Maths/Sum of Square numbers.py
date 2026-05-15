c = int(input("Enter number: "))

a = 0
b = int(c ** 0.5)

while a <= b:

    s = a * a + b * b

    if s == c:
        print(True)
        break

    elif s < c:
        a += 1

    else:
        b -= 1

else:
    print(False)