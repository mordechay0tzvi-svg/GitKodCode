def create_grades_file(filename):
    students = [
    ("Dan", [85, 90, 78]),
    ("MOMO", [92, 88, 95]),
    ("Yoni", [70, 65, 80]),
    ("Avi", [100, 95, 98]),
    ("Sara", [60, 72, 68]),
    ]
    with open(filename, "w") as f:
        for name, grades in students:
            line = name + "," + ",".join(map(str, grades)) + "\n"
            f.write(line)

create_grades_file('grades.txt')


def calculate_averages(filename):
    with open(filename) as f:
        students = f.readlines()
        averages = {}
        for student in students:
            student = student.split(',')
            grades =[]
            for grade in student[1:]:
                try:
                    grades.append(int(grade))
                except Exception as e:
                    print("careful: ", e)
            average = sum(grades) / len(grades)
            averages[student[0]] = average
    return averages

#print(calculate_averages("grades.txt"))

def save_results(averages, output_filename='results.txt'):
    averages = dict(sorted(averages.items(), key=lambda item: item[1], reverse=True))
    with open(output_filename, 'w') as f:
        for student, average in averages.items():
            f.write(f"{student}: {average} \n")

averages = calculate_averages('grades.txt')
save_results(averages, 'results.txt')


def statics(filename):
    with open(filename, 'r+') as f:
        students = f.readlines()
        averages = calculate_averages('grades.txt')
        max = ("" ,0)
        min = ("" ,100)
        passed = []
        count = 0
        sum = 0
        for student, average in averages.items():
            if average > max[1]:
                max = (student, average)
            elif average < min[1]:
                min = (student, average)
            if average >= 60:
                passed.append(student)
            count += 1
            sum += average
        f.write("======statistics===== \n")
        f.write(f"top score: {max} \n")
        f.write(f"lowest score: {min} \n")
        f.write(f'average: {sum/count} \n')
        f.write(f"passed: {passed} \n")

statics('results.txt')












