def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num

    return total

def calculate_average(numbers):
    total = calculate_sum(numbers)

    return total / len(numbers) if numbers else 0

def calculate_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
            return maximum
def calculate_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
            return minimum

numbers = [10, 20, 30, 40, 50]
print("Sum:", calculate_sum(numbers))
print("Average:", calculate_average(numbers))
print("Maximum:", calculate_max(numbers))
print("Minimum:", calculate_min(numbers))

              
