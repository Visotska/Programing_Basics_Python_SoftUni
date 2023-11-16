student_name = input()
grade_counter = 0
years_counter = 0
fails_counter = 0

while years_counter < 12:
    grades = float(input())

    if grades < 4:
        fails_counter += 1
        if fails_counter > 1:
            excluded_year = years_counter + 1
            print(f"{student_name} has been excluded at {excluded_year} grade")
            break
        continue

    grade_counter += grades
    years_counter += 1

else:
    average_grade = grade_counter / years_counter
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")