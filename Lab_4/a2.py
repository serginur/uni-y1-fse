n = m = ""
while (not n.isdigit() or not m.isdigit() or\
        n.count('-') or m.count('- ')\
        or n.startswith('0') or m.startswith('0')):
    try:
        n, m = input("Введите положительные целочисленные n и m: ").split()
    except ValueError:
        print("Введите 2 числа!")
        continue
    except (EOFError, KeyboardInterrupt):
        exit(0)
n = int(n)
m = int(m)

print(f"ПРЯМОУГОЛЬНИК {n}x{m}:")
for i in range(n):
    for j in range(m):
        print('#', end='')
    print()

print("\nПРАВЫЙ ТРЕУГОЛЬНИК")
for i in range(n):
    print('#'*(i + 1))

print(f"\nРАМКА {n}*{m}")
for i in range(n):
    for j in range(m):
        if i == 0 or i == n-1:
            print('#', end='')
        else:
            if j == 0 or j == m-1:
                print('#', end='')
            else:
                print(' ', end='')
    print()
