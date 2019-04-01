#try_except_block.py

print("please enter two numbers to be divided: ")
print("Enter 'q' to quit")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break

	second_number = input("\nSecond number: ")
	if first_number == 'q':
		break

	answer = int(first_number) / int(second_number)
	print(answer)