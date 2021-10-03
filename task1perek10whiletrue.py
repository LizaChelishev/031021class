# insert 10 different integer numbers
number_of_inserts = 0
previous_number = 0 
while True: 
    if number_of_inserts >= 10:
      break
    current_number = int(input('Insert integer number ' +str(number_of_inserts)+ ':'))
    if current_number < previous_number:
        print('Your list is not sorted.')
        break
    previous_number = current_number 
    number_of_inserts += 1

if number_of_inserts == 10:
    print('Your list is sorted')
