# insert numbers 10 different integer numbers
number_1 = int(input('Insert first integer number:'))
number_of_inserts = 1
while number_of_inserts < 10:
    number_2 = int(input('Insert second integer number:'))
    if number_2 < number_1:
        print('Your list is not sorted.')
        break
    number_1 = number_2
    number_of_inserts += 1

if number_of_inserts == 10:
    print('Your list is sorted')
