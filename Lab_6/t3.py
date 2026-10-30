import t1
import matplotlib.pyplot as plt
from dataclasses import dataclass

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
def draw_users_activity(users: list[dict], workouts: list[dict]):
    @dataclass
    class User:
        name: str
        workouts_num: int

    users_id_data: dict[int, User] = dict()
    for user in users:
        users_id_data[user["user_id"]] = User(user["name"], 0)
    for workout in workouts:
        users_id_data[workout["user_id"]].workouts_num += 1
    sorted_users = sorted(tuple(users_id_data.values()),
                          key=lambda us : us.workouts_num,
                          reverse=True)
    names = list()
    workouts_numbers = list()
    for user in sorted_users:
        names.append(user.name)
        workouts_numbers.append(user.workouts_num)
    plt.rcParams["axes.titleweight"] = "bold"
    plt.rcParams["figure.subplot.bottom"] = 0.2
    plt.rcParams["figure.subplot.left"] = 0.071
    plt.rcParams["figure.subplot.right"] = 0.98
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
def draw_workout_types_efficiency(workouts: list[dict]):
    @dataclass
    class WorkoutData:
        calories: int
        duration: int

    workout_types_data: dict[str, WorkoutData] = dict()
    for workout in workouts:
        w_type = workout["type"]
        if w_type in workout_types_data:
            workout_types_data[w_type].calories += workout["calories"]
            workout_types_data[w_type].duration += workout["duration"]
        else:
            workout_types_data[w_type] = WorkoutData(workout["calories"],
                                                workout["duration"])
    sorted_workout_types_data = sorted([[w_type,
                                         round(data.calories/data.duration, 2)]\
                              for w_type, data in workout_types_data.items()],
                              key=lambda item : item[1], reverse=True)
    workout_types = list()
    types_efficiency = list()
    for data in sorted_workout_types_data:
        workout_types.append(data[0])
        types_efficiency.append(data[1])
    plt.rcParams["axes.titleweight"] = "bold"
    plt.rcParams["figure.subplot.left"] = 0.06
    plt.rcParams["figure.subplot.right"] = 0.98
    plt.rcParams["figure.subplot.bottom"] = 0.31
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
def draw_users_compared_calories(users: list[dict], workouts: list[dict]):
    @dataclass
    class User:
        name: str
        level: str
        calories: int

    users_data: dict[int, User] = dict()
    for user in users:
        users_data[user["user_id"]] = User(user["name"],
                                           user["fitness_level"],
                                           0)
    for workout in workouts:
        users_data[workout["user_id"]].calories += workout["calories"]
    sorted_users_data = sorted([[user.name, user.level, user.calories]\
                               for user in users_data.values()],
                               key=lambda item : item[2], reverse=True)
    names = list()
    colors = list()
    labels = list()
    calories = list()
    num_to_color = {"начальный":    "tab:green",
                    "средний":      "tab:orange",
                    "продвинутый":  "tab:red"}
    for user_data in sorted_users_data:
        names.append(user_data[0])
        colors.append(num_to_color[user_data[1]])
        cap_label = user_data[1].capitalize()
        labels.append('_'+cap_label if cap_label in labels else cap_label)
        calories.append(user_data[2])
    plt.rcParams["axes.titleweight"] = "bold"
    plt.rcParams["figure.subplot.bottom"] = 0.2
    plt.rcParams["figure.subplot.right"] = 0.98
    plt.rcParams["figure.subplot.left"] = 0.09
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
    draw_total_workout_types(workouts)
    draw_users_activity(users, workouts)
    draw_workout_types_efficiency(workouts)
    draw_users_compared_calories(users, workouts)
