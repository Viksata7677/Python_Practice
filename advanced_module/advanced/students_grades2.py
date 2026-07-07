num_students = int(input())
students = {}
for student in range(num_students):
    student_info = input().split()
    name = student_info[0]
    grade = float(student_info[1])
    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    avg_grade = sum(grades)/len(grades)
    print(f'{name} -> {" ".join([f"{g:.2f}" for g in grades])} (avg: {avg_grade:.2f})')