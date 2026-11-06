import t1, t2
import matplotlib.pyplot as plt

# круговая диаграмма типов тренировок
def draw_total_workout_types(workouts: list[dict]):
    workout_types_amount: dict[str, int] = dict()
    for workout in workouts:
        w_type = workout["type"]
        workout_types_amount[w_type] = workout_types_amount.get(w_type, 0) + 1

    plt.rcParams["axes.titleweight"] = "bold"
    plt.title("Распределение типов тренировок")
    plt.pie(workout_types_amount.values(), labels=workout_types_amount.keys(),
            startangle=90, autopct="%1.1f%%")
    plt.show()

# столбчатая диаграмма активности пользователей (кол-во тренировок)
def draw_users_activity(users_activity: list[dict[str, str | int]]):
    sorted_users_activity = sorted([[user_data["name"], user_data["workouts"]]
                                    for user_data in users_activity],
                                    key=lambda user : user[1], reverse=True)

    names = list()
    workouts_numbers = list()
    for user in sorted_users_activity:
        names.append(user[0])
        workouts_numbers.append(user[1])

    plt.rcParams |= {
        "axes.titleweight": "bold",
        "figure.subplot.bottom": 0.2,
        "figure.subplot.left": 0.071,
        "figure.subplot.right": 0.98
    }
    plt.figure(figsize=(8, 5))
    bar_container = plt.bar(names, workouts_numbers, 
                            color=list("tab:cyan" for _ in range(len(names))))
    plt.bar_label(bar_container, fmt="{}")
    plt.title("Активность пользователей (количество тренировок)")
    plt.tick_params('x', rotation=45, rotation_mode="xtick")
    plt.xlabel("Пользователи")
    plt.ylabel("Количетво тренировок")
    plt.show()


# столбчатая диаграмма эффективности тренировок (ккал/мин)
def draw_workout_types_efficiency(workouts: dict[str, t2.AddEmpty0Dict[str, int]]):
    sorted_workout_types_data = sorted([[workout_type, 
                                         round(data["calories"]/data["duration"], 2)]
                                         for workout_type, data in workouts.items()],
                                         key=lambda item : item[1], reverse=True)
    workout_types = list()
    types_efficiency = list()
    for data_list in sorted_workout_types_data:
        workout_types.append(data_list[0])
        types_efficiency.append(data_list[1])

    plt.rcParams |= {
        "axes.titleweight": "bold",
        "figure.subplot.left": 0.06,
        "figure.subplot.right": 0.98,
        "figure.subplot.bottom": 0.31
    }
    plt.figure(figsize=(8, 5))
    bar_container = plt.bar(workout_types, types_efficiency,
                            color=list("tab:purple" for _ in range(len(workout_types))))
    plt.bar_label(bar_container, fmt="{:.2f}")
    plt.title("Эффективность тренировок (калории/минуту)")
    plt.tick_params('x', rotation=45, rotation_mode="xtick")
    plt.xlabel("Тип тренировки")
    plt.ylabel("Калории в минуту")
    plt.show()

# сравнительная диаграмма пользователей (общие ккал на пользователя)
def draw_users_compared_calories(users_data: list[dict[str, str|int]]):
    sorted_users_by_calories = sorted(users_data, key=lambda user: user["calories"],
                                      reverse=True)
    names = list()
    colors = list()
    labels = list()
    calories = list()
    fit_level_to_color = {"начальный":    "tab:green",
                          "средний":      "tab:orange",
                          "продвинутый":  "tab:red"}
    for user_dict in sorted_users_by_calories:
        names.append(user_dict["name"])
        colors.append(fit_level_to_color[user_dict["level"]])
        cap_label = user_dict["level"].capitalize()
        labels.append('_'+cap_label if cap_label in labels else cap_label)
        calories.append(user_dict["calories"])

    plt.rcParams |= {
        "axes.titleweight": "bold",
        "figure.subplot.bottom": 0.2,
        "figure.subplot.right": 0.98,
        "figure.subplot.left": 0.09
    }
    plt.figure(figsize=(8, 5))
    bar_container = plt.bar(names, calories, label=labels, color=colors)
    plt.bar_label(bar_container, fmt="{:,}")
    plt.title("Эффективность тренировок (калории/минуту)")
    plt.tick_params('x', rotation=45, rotation_mode="xtick")
    plt.xlabel("Пользователи")
    plt.ylabel("Общие калории")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    users = t1.load_users_data()
    workouts = t1.load_workouts_data()
    users_activity = t2.get_users_activity(users, workouts)
    workout_types = t2.get_workout_types(workouts)
    draw_total_workout_types(workouts)
    draw_users_activity(users_activity)
    draw_workout_types_efficiency(workout_types)
    draw_users_compared_calories(users_activity)
