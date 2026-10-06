from random import randint
import time
from sys import argv

n = None
if (len(argv) > 1):
    if (argv[1] != "inf"):
        try:
            n = int(argv[1])
        except ValueError:
            print(f"usage: python {argv[0]} [num] ")
            print("where [num] is a natural number or 'inf' for infinity")
            print("Ctrl-D or Ctrl-C to exit")
            exit(0)
    else:
        n = True

if (n is None):
    is_ok_input = False
    while not is_ok_input:
        n = input("Введите количество примеров или \"inf\" для бесконечных примеров: ")
        if n == "inf":
            n = True
            is_ok_input = True
        elif n.isdigit():
            n = int(n)
            is_ok_input = True
        else:
            print("Неверный ввод!")

programm_start_time = time.time()
tasks_times = []
right_answers = 0
i = 0
while True:
    i += 1
    print(f"Вопрос {i}{f"/{n}" if n is int else ""}")
    a = randint(2, 9)
    b = randint(2, 9)

    start_time = time.time()
    answer = None
    is_interrupted = False
    while True:
        try:
            answer = input(f"{a} * {b} = ")
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")
        except (KeyboardInterrupt, EOFError):
            is_interrupted = True
            i -= 1
            break
    if (is_interrupted): 
        print()
        break
    spend_time = time.time() - start_time
    if int(answer) == a*b:
        print(f"Верно! (Время: {spend_time:.1f} секунд)")
        right_answers += 1
    else:
        print(f"Неверно! Правильно: {a*b} (Время: {spend_time:.1f} секунд)")

    if (n is int and i == n):
        break


programm_spend_time = time.time() - programm_start_time
print("="*30)
print("СТАТИСТИКА:")
print("="*30)
print(f"Общее время: {programm_spend_time:.1f} секунд")
print(f"Среднее время на вопрос: {programm_spend_time/n:.1f} секунд")
print(f"Правильных ответов: {right_answers}/{i}")
try:
    right_percent = right_answers/i
except ZeroDivisionError:
    right_percent = 0
print(f"Процент правильных: {right_percent * 100:.1f}%")
