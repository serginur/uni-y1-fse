import t1

# кастомный класс, наследующий из словаря, единственное отличие которого
# от dict в том, что при обращении через [] к его отсутствующему ключу
# создается новое значение по этому ключу и предполагаемые операции
# производятся уже с новосозданным элементом
class AddEmpty0Dict(dict):
    def __missing__(self, key):
        return 0

def analyze_user_activity(users: list[dict], workouts: list[dict]):
    total_users_workouts: list[dict] = list()
    for user in users:
        workouts_num = calories = duration = 0
        for workout in workouts:
            if workout["user_id"] == user["user_id"]:
                workouts_num += 1
                calories += workout["calories"]
                duration += workout["duration"]
        duration /= 60

        total_users_workouts.append({"name": user["name"],
                                     "level": user["fitness_level"],
                                     "workouts": workouts_num,
                                     "calories": calories, 
                                     "duration": duration})

    total_users_workouts = sorted(total_users_workouts,\
                                  key=lambda user: user["workouts"], reverse=True)

    print("ТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
    for i in range(3):
        user = total_users_workouts[i]
        print(f"  {i+1}. {user["name"]} ({user["level"]}):")
        print(f"    Тренировок: {user["workouts"]}")
        print(f"    Калорий: {user["calories"]}")
        print(f"    Время: {user["duration"]:.1f} часов\n")

def analyze_workout_types(workouts):
    workout_types: dict[str, AddEmpty0Dict[str, int]] = dict()
    for workout in workouts:
        type_dict = workout_types.setdefault(workout["type"], AddEmpty0Dict())
        # так как использован кастомный класс, ошибки при обращении к отсутсвующему
        # элементу не будет:
        type_dict["amount"] += 1
        type_dict["duration"] += workout["duration"]
        type_dict["calories"] += workout["calories"]

    # сортировка по средней длительности
    workout_types = sorted(workout_types.items(),
                key=lambda w_t_tuple: w_t_tuple[1]["duration"]/w_t_tuple[1]["amount"],
                                reverse=True)

    print("РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
    for workout_type, type_params in workout_types:
        print(f"  {workout_type.capitalize()}: {type_params["amount"]} тренировок ({type_params["amount"]*100/len(workouts):.1f}%)")
        print(f"    Средняя длительность: {round(type_params["duration"]/type_params['amount'])} мин")
        print(f"    Средние калории: {round(type_params["calories"]/type_params['amount'])} ккал")
    print()

def find_user_workouts(users: list[dict], workouts: list[dict], user_name: str):
    user_id = None
    for user in users:
        if user["name"].casefold() == user_name.casefold():
            user_id = user["user_id"]
            break

    user_workouts: list[dict] = list()
    if user_id:
        for workout in workouts:
            if workout["user_id"] == user_id:
                user_workout = workout.copy()
                del user_workout["workout_id"], user_workout["user_id"]
                user_workouts.append(user_workout)

    if user_workouts:
        print(f"ВСЕ ТРЕНИРОВКИ ПОЛЬЗОВАТЕЛЯ: {user_name}")
        for workout in user_workouts:
            print(f" >{workout["date"].strftime(r"%d.%m.%Y")}: {workout["type"].capitalize()} в течение {workout["duration"]} мин, интенсивность: {workout["intensity"]}")
            if workout["distance"]:
                print(f"{' '*14}Дистанция: {workout["distance"]} км")
            print(f"{' '*14}Калорий сожжено: {workout["calories"]} ккал")
            print(f"{' '*14}Средний пульс: {workout["avg_heart_rate"]}")
    elif user_id:
        print(f"Тренировки пользователя \"{user_name}\" не найдены.")
    else:
        print(f"Пользователь \"{user_name}\" не найден.")
    print()

def analyze_user(user: str, users: list[dict], workouts: list[dict]):
    user_info: dict = None
    for user_dict in users:
        if user_dict["name"].casefold() == user.casefold():
            user_info = user_dict.copy()
            del user_info["name"], user_info["workouts"]
            user_info["types"] = dict()
            break

    # ссылка на словарь с типами тренировок пользователя
    user_types = user_info["types"]
    for workout in workouts:
        if workout["user_id"] == user_info["user_id"]:
            user_info["workouts"] = user_info.setdefault("workouts", 0) + 1
            for key in ("calories", "duration", "distance"):
                user_info[key] = user_info.setdefault(key, 0) + workout[key]
            # ссылка на "новый" словарь
            workout_type_dict = user_types.setdefault(workout["type"], AddEmpty0Dict())
            workout_type_dict["amount"] += 1
            workout_type_dict["duration"] += workout["duration"]

    if user_info.get("workouts"):
        types_max_amount = max(type_data["amount"] for type_data in user_types.values())
        favorite_types: list[dict] = list()
        for type_name, type_data in user_types.items():
            if type_data["amount"] == types_max_amount:
                favorite_types.append({"type_name": type_name,
                                        "amount": type_data["amount"],
                                        "duration": type_data["duration"]})

        favorite_type = ''
        if len(favorite_types) == 1:
            favorite_type = favorite_types[0]["type_name"]
        else:
            max_duration = max(type_dict["duration"] for type_dict in favorite_types)
            for type_dict in favorite_types:
                if type_dict["duration"] == max_duration:
                    favorite_type = type_dict["type_name"]

        print(f"ДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user}")
        print('='*43)
        print(f"Возраст: {user_info["age"]} лет, Вес: {user_info["weight"]} кг")
        print(f"Уровень: {user_info["fitness_level"]}")
        print(f"Тренировок: {user_info["workouts"]}")
        print(f"Сожжено калорий: {user_info["calories"]}")
        print(f"Общее время: {user_info["duration"]/60:.1f} часов")
        print(f"Пройдено дистанции: {user_info["distance"]:.1f} км")
        print(f"Средние калории за тренировку: {round(user_info["calories"]/user_info["workouts"])}")
        print(f"Любимый тип тренировки: {favorite_type}")
    elif user_info:
        print(f"Тренировки пользователя \"{user}\" не найдены.")
    else:
        print(f"Пользователь \"{user}\" не найден.")
    print()

if __name__ == "__main__":
    users = t1.load_users_data()
    workouts = t1.load_workouts_data()
    analyze_user_activity(users, workouts)
    analyze_workout_types(workouts)
    find_user_workouts(users, workouts, "Анна")
    analyze_user("Борис", users, workouts)
