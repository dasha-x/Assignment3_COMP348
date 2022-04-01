# def lucas_sequence(num):
#     a, b = 2, 1
#
#     for i in range(0, num):
#         print(a, end=' ')
#         a, b = b, a + b
#     print()


def lucas(num):
    a, b = 2, 1

    while a < num:
        print(a, end=' ')
        a, b = b, a + b
    print()


lucas_sequence(3)
lucas_sequence(5)
lucas(11)
lucas(10)
