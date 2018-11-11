figure = input()
if figure == "прямоугольник":
    a = int(input())
    b = int(input())
    print(float(a * b))
elif figure == "круг":
    r = int(input())
    print(3.14 * r ** 2)
elif figure == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p=(a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)