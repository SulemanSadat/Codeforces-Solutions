def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

for index, x in enumerate(fib()):
    if index == 10:
        break
    print("%s" % x),
# def fa(numbers):
#     jan = 3
#     for c in numbers:
#         for d in range(1, len(numbers)):
#             if c < numbers[d]:
#                 print(True)
#
#             elif c > numbers[d]:
#                 print(False)
#
#                 print(c)
#                 jan -= 1
#
#
#         if jan < 0:
#             break
#     print(jan)
#
#
# n = [1, 2, 4, 3, 6]
#
# fa(n)
