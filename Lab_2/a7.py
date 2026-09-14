a = int(input("Введите первую координату первой клетки: "))
b = int(input("Введите вторую координату первой клетки: "))
c = int(input("Введите первую координату второй клетки: "))
d = int(input("Введите вторую координату второй клетки: "))

first = "White" if (a%2 == 1 and b%2 == 1 or a%2 == 0 and b%2 == 0) else "Black"
second = "White" if (c%2 == 1 and d%2 == 1 or c%2 == 0 and d%2 == 0) else "Black"

if (first == second):
    print("YES", first, sep='\n')
else:
    print("NO")
