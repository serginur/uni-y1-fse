import t1

def analyze_user_activity(users: list[dict], workouts: list[dict]):
    total_users_workouts: list[list] = list()
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
    total_users_workouts = sorted(total_users_workouts,\
                                  key=lambda user: user[2], reverse=True)
    print("ТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
    for i in range(3):
        user = total_users_workouts[i]
        print(f"  {i+1}. {user[0]} ({user[1]}):")
        print(f"    Тренировок: {user[2]}")
        print(f"    Калорий: {user[3]}")
        print(f"    Время: {user[4]:.1f} часов\n")

def analyze_workout_types(workouts):
    types_of_workouts: dict[str, dict[str, int]] = dict()
    for workout in workouts:
        workout_type = workout["type"]
        if workout_type in types_of_workouts:
            # ссылка на словарь текущего типа тренировки
            type_dict = types_of_workouts[workout_type]
            type_dict["amount"] += 1
            type_dict["duration"] += workout["duration"]
            type_dict["calories"] += workout["calories"]
        else:
            types_of_workouts[workout_type] = {"amount": 1,
                                               "duration": workout["duration"],
                                               "calories": workout["calories"]}
    # сортировка по длительности
    types_of_workouts = sorted(types_of_workouts.items(),\
                key=lambda w_t_tuple: w_t_tuple[1]["duration"]/w_t_tuple[1]["amount"],\
                                reverse=True)
    print("РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
    for workout_type, type_params in types_of_workouts:
        print(f"  {workout_type.capitalize()}: {type_params["amount"]} тренировок ({type_params["amount"]*100/len(workouts):.1f}%)")
        print(f"    Средняя длительность: {round(type_params["duration"]/type_params['amount'])} мин")
        print(f"    Средние калории: {round(type_params["calories"]/type_params['amount'])} ккал")

def find_user_workouts(users: list[dict], workouts: list[dict], user_name: str):
    is_found_user = False
    is_found_workouts = False
    user_workouts: list[dict] = list()
    for user in users:
        if user["name"].casefold() == user_name.casefold():
            is_found_user = True
            for workout in workouts:
                if workout["user_id"] == user["user_id"]:
                    if not is_found_workouts:
                        is_found_workouts = True
                    user_workout = workout.copy()
                    del user_workout["workout_id"], user_workout["user_id"]
                    user_workouts.append(user_workout)
            if is_found_user:
                break
    if is_found_workouts:
        print(f"ВСЕ ТРЕНИРОВКИ ПОЛЬЗОВАТЕЛЯ: {user_name}")
        for workout in user_workouts:
            print(f" >{workout["date"].strftime(r"%d.%m.%Y")}: {workout["type"].capitalize()} в течение {workout["duration"]} мин, интенсивность: {workout["intensity"]}")
            if workout["distance"]:
                print(f"{' '*14}Дистанция: {workout["distance"]} км")
            print(f"{' '*14}Калорий сожжено: {workout["calories"]} ккал")
            print(f"{' '*14}Средний пульс: {workout["avg_heart_rate"]}")
    elif is_found_user:
        print(f"Тренировки пользователя \"{user_name}\" не найдены.")
    else:
        print(f"Пользователь \"{user_name}\" не найден.")
    print()

def analyze_user(user: str, users: list[dict], workouts: list[dict]):
    is_found_user = False
    is_found_workouts = False
    user_info: dict = None
    for user_d in users:
        if user_d["name"].casefold() == user.casefold():
            is_found_user = True
            user_info = user_d.copy()
            del user_info["user_id"], user_info["name"], user_info["workouts"]
            user_info["types"] = dict()
            for workout in workouts:
                if workout["user_id"] == user_d["user_id"]:
                    if not is_found_workouts:
                        is_found_workouts = True
                    user_info["workouts"] = user_info.setdefault("workouts", 0) + 1
                    for key in ["calories", "duration", "distance"]:
                        user_info[key] = user_info.setdefault(key, 0) + workout[key]
                    if workout["type"] not in user_info["types"]:
                        user_info["types"][workout["type"]] = [1, workout["duration"]]
                    else:
                        user_info["types"][workout["type"]][0] += 1
                        user_info["types"][workout["type"]][1] += workout["duration"]
            if is_found_user:
                break
    if is_found_workouts:
        print(f"ДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user}")
        print('='*43)
        print(f"Возраст: {user_info["age"]} лет, Вес: {user_info["weight"]} кг")
        print(f"Уровень: {user_info["fitness_level"]}")
        print(f"Тренировок: {user_info["workouts"]}")
        print(f"Сожжено калорий: {user_info["calories"]}")
        print(f"Общее время: {user_info["duration"]/60:.1f} часов")
        print(f"Пройдено дистанции: {user_info["distance"]:.1f} км")
        print(f"Средние калории за тренировку: {round(user_info["calories"]/user_info["workouts"])}")
        fav_types = ' '.join(key for key, val in user_info["types"].items() if val[0] == max(type_info[0] for type_info in user_info["types"].values()))
        if len(fav_types.split()) > 1:
            max_duration = max(type_info[1] for workout_type, type_info in user_info["types"].items() if workout_type in fav_types)
            for workout_type, type_info in user_info["types"].items():
                if type_info[1] == max_duration:
                    fav_types = workout_type
        print(f"Любимый тип тренировки: {fav_types}")
    elif is_found_user:
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
    analyze_user("Григорий", users, workouts)
