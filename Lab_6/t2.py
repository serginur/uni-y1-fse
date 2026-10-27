import t1

def analyze_user_activity(users: list[dict], workouts: list[dict]):
    total_users_workouts = list()
    for user in users:
        workouts_num = 0
        calories = 0
        duration = 0
        for workout in workouts:
            if workout["user_id"] == user["user_id"]:
                workouts_num += 1
                calories += workout["calories"]
                duration += workout["duration"]
        duration /= 60
        total_users_workouts.append([user["name"],
                                     user["fitness_level"],
                                     workouts_num,
                                     calories,
                                     duration])
    total_users_workouts = sorted(total_users_workouts, key=lambda user: user[2], reverse=True)
    print("ТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
    for i in range(3):
        user = total_users_workouts[i]
        print(f"  {i+1}. {user[0]} ({user[1]}):")
        print(f"    Тренировок: {user[2]}")
        print(f"    Калорий: {user[3]}")
        print(f"    Время: {user[4]:.1f} часов")
        if i != 2:
            print()

def analyze_workout_types(workouts):
    pass
    # выведет распределение по типам тренировок в следующем виде:
    # РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:
    #   Бег: 13 тренировок (19.4%)
    #     Средняя длительность: 62 мин
    #     Средние калории: 575 ккал
    #   Силовая тренировка: 13 тренировок (19.4%)
    #     Средняя длительность: 56 мин
    #     Средние калории: 343 ккал
    #   Велосипед: 18 тренировок (26.9%)
    #     Средняя длительность: 53 мин
    #     Средние калории: 366 ккал
    #   Плавание: 5 тренировок (7.5%)
    #     Средняя длительность: 46 мин
    #     Средние калории: 368 ккал
    #   Ходьба: 18 тренировок (26.9%)
    #     Средняя длительность: 39 мин
    #     Средние калории: 196 ккал

def find_user_workouts(users, user_name): # TODO: ОТКУДА В ЮЗЕРАХ ДАННЫЕ О ТРЕНИРОВКАХ???
    pass
    # находит и возвращает все тренировки пользователя по имени

def analyze_user(user, workouts): # TODO: ОТКУДА В ВОРКАУТАХ ДАННЫЕ О ПОЛЬЗОВАТЕЛЕ???
    pass
    # выводит детальный анализ тренировок пользователя по имени в следующем виде:
    # ДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: Борис
    # ===========================================
    # Возраст: 35 лет, Вес: 82 кг
    # Уровень: средний
    # Тренировок: 9
    # Сожжено калорий: 2750
    # Общее время: 7.4 часов
    # Пройдено дистанции: 64.3 км
    # Средние калории за тренировку: 306
    # Любимый тип тренировки: ходьба

if __name__ == "__main__":
    users = t1.load_users_data()
    workouts = t1.load_workouts_data()
    analyze_user_activity(users, workouts)
