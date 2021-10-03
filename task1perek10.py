# insert numbers 10 different integer numbers
current_number = int(input('Insert integer number:'))
number_of_inserts = 1
while number_of_inserts < 10:
    next_number = int(input('Insert integer number:'))
    if next_number < current_number:
        print('Your list is not sorted.')
        break
    current_number = next_number
    number_of_inserts += 1

if number_of_inserts == 10:
    print('Your list is sorted')
