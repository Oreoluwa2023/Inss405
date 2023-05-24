num_users = 3
grades = [float(input("Enter final grade for user: ".format(i + 1))) for i in range(num_users)]

total_sum = sum(grades) / len(grades)

print("Mean: ", total_sum)

if total_sum >= 90:
    print("Grade: A")
elif total_sum >= 80:
    print("Grade: B")
elif total_sum >= 70:
    print("Grade: C")
elif total_sum >= 60:
    print("Grade: D")
else:
    print("Grade: F")
