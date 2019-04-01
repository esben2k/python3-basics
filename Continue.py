#Continue statement

current_number = 0
while current_number < 10:
    current_number += 1

    #modulus 2 - the second digit of the number
    if current_number % 2 == 0:
        continue

print(current_number)
