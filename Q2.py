def lucas_sequence(num):
    a, b = 2, 1

    for i in range(0, num):
        print(a, end=' ')
        a, b = b, a + b
    print()


def lucas_generator(num):
    a, b = 2, 1

    for i in range(num):
        yield a
        a, b = b, a + b


lucas_sequence(6)

for num in lucas_generator(6):
    print(num, end=' ')
print()
