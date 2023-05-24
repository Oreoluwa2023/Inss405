import random as rand
num = 100
numbers = [rand.randint(1, 100) for i in range(num)]

def sort_num(num):
    sort_number = sorted(num)
    return sort_number

print("Random Numbers:", numbers)
sorted_numbers = sort_num(numbers)

print("Sorted Numbers:", sorted_numbers)


