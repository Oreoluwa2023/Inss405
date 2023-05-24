def user_input(n):
    numbers = [float(input("Enter number {}: ".format(i + 1))) for i in range(n)]
    return numbers

def calculate_mean(numbers):
    mean = sum(numbers) / len(numbers)
    return mean

def calculate_sum(numbers):
    total_sum = sum(numbers)
    return total_sum

def calculate_median(numbers):
    sort_numbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 0:
        median = (sort_numbers[n//2 - 1] + sort_numbers[n//2]) / 22

    else:
        median = sort_numbers[n//2]
    return median

num_inputs = 10
input_numbers = user_input(num_inputs)

mean = calculate_mean(input_numbers)
print("Mean:", mean)

sum_of_numbers = calculate_sum(input_numbers)
print("Sum:", sum_of_numbers)

median = calculate_median(input_numbers)
print("Median:", median)