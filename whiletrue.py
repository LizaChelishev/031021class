# input grades until the garde is <= -1
_sum = 0
_avg = 0
number_of_grades = 0

while True : #do-while
    if number_of_grades > 40:
        break
    grade = int(input('please enter a grade:'))
    if grade == -1:
        break
    if grade == 0:
        continue
        _sum += grade
    number_of_grades += 1
    _avg = _sum / number_of_grades
    if _avg == 99:
        break

