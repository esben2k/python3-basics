#list_of_numbers.py

# Converting numbers to list
numbers = list(range(1,6))
print(numbers)

# 2 = adding 2 up until 101
odd_numbers = list(range(1,101, 2))
print(odd_numbers)

squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)
print(squares)

digits = [1,2,3,4,5]
print(sum(digits))

