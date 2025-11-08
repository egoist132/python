# pr1=int(input("первое число?"))
# pr2=int(input("второе число?"))
# pr3=int(input("третье число?"))
# if pr2-pr1==pr3-pr2:
#     print("YES")
# else:
#     print("NO")


# pr1=int(input("первое число?"))
# pr2=int(input("второе число?"))
# pr3=int(input("третье число?"))
# print(min(pr1,0)+min(pr2,0)+min(pr3,0))
# pr4=0
# if pr1 > 0:
#     pr4+=pr1
# if pr2 > 0:
#     pr4=pr4+pr2
# if pr3 > 0:
#     pr4=pr4+pr3
# else:
#     print(0)
# print(pr4)
# if pr1 >= 100 and pr1<=999:
#     print("являеться")

# x=int(input("число"))
# y=int(input("число"))

# if x > 0 and y>0:
#     print("1 четверть")
# if x > 0 and y < 0:
#     print("4 четверть")
# if x <0 and y <0:
#     print("3 четверть")
# if x < 0 and y > 0:
#     print("2 четверть")


# chs1=int(input("число"))
# chs2=chs1//100
# chs3=chs1%10
# chs4=chs1%100//10

# if chs2==chs3 and chs2==chs4 and chs3==chs4:
#     print("одинаковые")
# else:
#     print("различные")


# chs1=int(input("число?"))

# if chs1 >= -1 and chs1 <= 17:
#     print("принадлежит")
# else:
#     print("не принадлежит")

# chs1=int(input("число?"))

# if chs1 >= 7 or chs1 <= -3:
#     print("принадлежит")
# else:
#     print("не принадлежит")


# chs1=int(input("число?"))

# if (chs1 >= 1000 and chs1 <=9999) and (chs1%7==0 or chs1%17==0):
#     print("YES")
# else:
#     print("NO")

# if chs1%4==0 and not(chs1%100==0) or chs1%100==0:
#     print("yes")
# else:
#     print("NO")

# x1=int(input("координата?"))
# y1=int(input("S"))
# x2=int(input("S"))
# y2=int(input("S"))

# if x1 == x2 or y1==y2:
#     print("ладия")
# else:
#     print("не ладья")


# chs1=float(input("число?"))

# if (chs1 <=25 and chs1 >=7) or chs1 >= -30 and chs1 <= -2:
#     print("YES")
# else:
#     print("NO")

# a, b, c = int(input()), int(input()), int(input())

# if a == b == c:
#     print(3)
# elif a == b:
#     print(2)
# elif a == c:
#     print(2)
# elif b == c:
#     print(2)
# else:
#     print(0)


# a, b = int(input()), int(input())

# if a < b:
#     print("NO")
# elif b > a:
#     print("YES")
# else:
#     print("Dont know")


# a, b, c = int(input()), int(input()), int(input())

# if a == b == c:
#     print("Равносторонний")
# elif a == b:
#     print("Равнобедренный")
# elif a == c:
#     print("Равнобедренный")
# elif b == c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")




# if a > b >c or c > b >a:
#     print(b)
# elif b > a >c or c> a> b:
#     print(a)
# else:
#     print


a=int(input("месяц"))

if a == 2:
    print("28")
elif a == 1 or 3 or 5 or 7 or 9 or 11:
    print(31)
elif a == 4 or 6 or 8 or 10 or 12:
    print(30)