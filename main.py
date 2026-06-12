import json
students = [
    {"id": 1, "name": "Alice", "age": 20},
    {"id": 2, "name": "Bob", "age": 21},
    {"id": 3, "name": "Charlie", "age": 19},
    {"id": 4, "name": "David", "age": 22},
    {"id": 5, "name": "Emma", "age": 20}
]
with open("students.json", "w") as file:
    json.dump(students, file, indent=2)
print("Data saved to students.json")
with open("students.json", "r") as file:
    loaded_students = json.load(file)
print("\nData read from students.json:")
for student in loaded_students:
    print(student)