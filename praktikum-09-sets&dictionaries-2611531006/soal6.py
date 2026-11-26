schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

# --- Soal 6a ---
# Mencari hari dengan jumlah mata kuliah terbanyak
busiest_day = max(schedule, key=lambda day: len(schedule[day]))
max_courses = len(schedule[busiest_day])

print(f"Busiest day: {busiest_day} ({max_courses} courses)")

# --- Soal 6b ---
# Meminta input mata kuliah dan menghitung berapa hari mata kuliah tersebut muncul
course_input = input("Masukkan nama mata kuliah: ")
day_count = 0

for courses in schedule.values():
  if course_input in courses:
    day_count += 1

print(f"{course_input}: {day_count} days")