# x=float(input())
# from math import ceil, floor

# print(ceil(x)+floor(x))

# from math import *  # Импортирует все функции из модуля math, чтобы использовать их в коде
# # получаем четыре вещественных числа сохраняем их в переменные 'x1', 'y1', 'x2' и 'y2'
# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
# # Вычисляет квадрат разности координат по оси x 
# q = pow(x1 - x2, 2)
# # Вычисляет квадрат разности координат по оси y 
# w = pow(y1 - y2, 2)
# # Вычисляет квадратный корень из суммы квадратов разностей координат по осям x и y, используя функцию sqrt()
# p = sqrt(q + w)
# # Выводит на экран расстояние между точками (x1, y1) и (x2, y2).
# print(p)

# from math import sqrt,pow
# a,b,c,d= float(input()),float(input()),float(input()),float(input())

# print(sqrt(pow(a-b, 2)+pow(c-d, 2)))


# a,b=float(input()),float(input())
# from math import sqrt,pow

# print((a+b)/2)
# print(sqrt(a*b))
# print((2*a*b)/(a+b))
# print(sqrt((pow(a,2)+pow(b,2))/2))


# from math import pow,pi,tan
# a,b=float(input()),float(input())

# print((a*pow(b,2))/4*tan(pi/a))


# from math import radians,sin,cos,tan

# b=radians(float(input()))


# print(sin(b)+cos(b)+pow(tan(b),2))

from math import sqrt,pow
a,b,c=float(input()),float(input()),float(input())
d=pow(b,2)-4*a*c

if d < 0:
    print("Нельзя решить")
elif d == 0:
    print('будет один корень ', -b/2*a)
elif d > 0:
    print((-b-sqrt(d))/2*a)
    print((-b+sqrt(d))/2*a)