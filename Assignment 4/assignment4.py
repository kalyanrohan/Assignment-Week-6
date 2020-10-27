eren = {
  "name": "Eren",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
mikasa = {
 "name": "Mikasa",
 "homework": [100.0, 92.0, 98.0, 100.0],
 "quizzes": [82.0, 83.0, 91.0],
 "tests": [89.0, 97.0]
}

armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}

students=[eren,mikasa,armin]

for student in students:
    for key in student:
        print(student[key])
def average(numbers):
    total=float(sum(numbers))
    result=total/len(numbers)
    return result

def get_average(student):
    homework=average(student['homework'])
    quizzes=average(student['quizzes'])
    tests=average(student['tests'])
    homework_weight= homework*10/100
    quizzes_weight= quizzes*30/100
    tests_weight= tests*60/100
    total_score= homework_weight+quizzes_weight+tests_weight
    return total_score
print(get_average(eren))

def get_letter_grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return"F"

grade= get_letter_grade(get_average(eren))
print(grade)


def get_class_average(students):
    results=[]
    for student in students:
        results.append(get_average(student))
    results=average(results)
    return results
print(f'class average: {get_class_average(students)}')
print(f'class grade: {get_letter_grade(get_class_average(students))}')
    



