from random import randint
import time

n = int(input("Введите количество примеров: "))

programm_start_time = time.time()
tasks_times = []
right_answers = 0
for i in range(n):
    print(f"Вопрос {i+1}/{n}")
    a = randint(2, 9)
    b = randint(2, 9)

    start_time = time.time()
    answer = None
    while True:
        try:
            answer = input(f"{a} * {b} = ")
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")
    spend_time = time.time() - start_time
    if int(answer) == a*b:
        print(f"Верно! (Время: {spend_time:.1f} секунд)")
        right_answers += 1
    else:
        print(f"Неверно! Правильно: {a*b} (Время: {spend_time:.1f} секунд)")

programm_spend_time = time.time() - programm_start_time
print("="*30)
print("СТАТИСТИКА:")
print("="*30)
print(f"Общее время: {programm_spend_time:.1f} секунд")
print(f"Среднее время на вопрос: {programm_spend_time/n:.1f} секунд")
print(f"Правильных ответов: {right_answers}/{n}")
print(f"Процент пралвильных: {right_answers/n * 100:.1f}%")
