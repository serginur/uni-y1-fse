import t1
import matplotlib.pyplot as plt

# круговая диаграмма типов тренировок
def draw_total_workout_types(workouts: list[dict]):
    pass

# столбчатая диаграмма активности пользователей (кол-во тренировок)
def draw_users_activity(users: list[dict], workouts: list[dict]):
    pass

# столбчатая диаграмма эффективности тренировок (ккал/мин)
def draw_workout_types_effectivity(workouts: list[dict]):
    pass

# сравнительная диаграмма пользователей (общие ккал на пользователя)
def draw_users_compared_calories(users: list[dict], workouts: list[dict]):
    pass

if __name__ == "__main__":
    users = t1.load_users_data()
    workouts = t1.load_workouts_data()
    draw_total_workout_types(workouts)
    draw_users_activity(users, workouts)
    draw_workout_types_effectivity(workouts)
    draw_users_compared_calories(users, workouts)
