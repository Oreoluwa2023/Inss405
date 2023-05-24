import random as rand

num = 100
numbers = [rand.randint(1, 100) for i in range(num)]

odd_numbers = [num for num in numbers if num % 2 != 0]

# Print the odd numbers
print(odd_numbers)




