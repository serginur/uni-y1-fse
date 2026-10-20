import xml.etree.ElementTree as ET
from sys import argv
from datetime import date as d

users_file = "task_files/users.xml"
workouts_file = "task_files/workouts.xml"
if len(argv) > 1:
    if len(argv) < 4:
        users_file = argv[1]
        workouts_file = argv[2]
    else:
        print(f"!-- usage: python {argv[0]} [path_to_users path_to_workouts]")
        exit(0)

def load_users_data():
    try:
        users_tree = ET.parse(users_file)
        users = []
        for user_elem in users_tree.getroot().findall("user"):
            user = {
                "user_id": int(user_elem.find("user_id").text),
                "name": user_elem.find("name").text,
                "age": int(user_elem.find("age").text),
                "weight": int(user_elem.find("weight").text),
                "fitness_level": user_elem.find("fitness_level").text,
                "workouts": []
            }
            users.append(user)
        return users
    except FileNotFoundError:
        print("Файл не найден!")
        return []

def load_workouts_data():
    try:
        workouts_tree = ET.parse(workouts_file)
        workouts = []
        for workout_elem in workouts_tree.getroot().findall("workout"):
            workout = {
                "workout_id": int(workout_elem.find("workout_id").text),
                "user_id": int(workout_elem.find("user_id").text),
                "date": d.strptime(workout_elem.find("date").text, "%Y-%m-%d"),
                "type": workout_elem.find("type").text,
                "duration": float(workout_elem.find("duration").text),
                "distance": float(workout_elem.find("distance").text),
                "calories": int(workout_elem.find("calories").text),
                "avg_heart_rate": int(workout_elem.find("avg_heart_rate").text),
                "intensity": workout_elem.find("intensity").text
            }
            workouts.append(workout)
        return workouts
    except FileNotFoundError:
        print("Файл не найден!")
        return []

def get_status():
    users = load_users_data()
    workouts = load_workouts_data()
    total_calories = 0
    total_duration = 0
    total_distance = 0.0
    for workout in workouts:
        total_calories += workout["calories"]
        total_duration += workout["duration"]
        total_distance += workout["distance"]
    total_duration = total_duration / 60
    print("ОБЩАЯ СТАТИСТИКА\n===========================")
    print(f"Всего тренировок: {len(workouts)}")
    print(f"Всего пользователей: {len(users)}")
    print(f"Сожжено калорий: {total_calories}")
    print(f"Общее время: {total_duration:.01f} часов")
    print(f"Пройдено дистанции: {total_distance:.01f} км")

if __name__ == "__main__":
    get_status()
