def is_ascending(numbers):
    return all(numbers[i] < numbers[i + 1] and abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))

def is_descending(numbers):
    return all(numbers[i] > numbers[i + 1] and abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))

def can_be_made_safe(numbers):
    for i in range(len(numbers)):
        new_numbers = numbers[:i] + numbers[i+1:]
        if is_ascending(new_numbers) or is_descending(new_numbers):
            return True
    return False

safe_counter = 0

with open("day2_input.txt", "r") as input_file:
    lines = input_file.readlines()

for line in lines:
    numbers = list(map(int, line.split()))
    if is_ascending(numbers) or is_descending(numbers):
        safe_counter += 1
        print(f"The line {numbers} is safe")
    elif can_be_made_safe(numbers):
        safe_counter += 1
    else:
        print(f"The line {numbers} is not safe")

print(f"Total valid lines: {safe_counter}")
