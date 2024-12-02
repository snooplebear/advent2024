safe_counter = 0

with open("day2_input.txt", "r") as input_file:
    lines = input_file.readlines()

for line in lines:
    numbers = list(map(int, line.split()))

    is_ascending = all(numbers[i] < numbers[i + 1] and abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))
    
    is_descending = all(numbers[i] > numbers[i + 1] and abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))
    
    if is_ascending or is_descending:
        safe_counter += 1
        print(f"Current safe count: {safe_counter}")

def is_descending(numbers):
   return all(numbers[i] < numbers[i + 1] and abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))

def is_ascending(numbers):
   return all(numbers[i] < numbers[i + 1] and abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))

print(f"Total safe lines: {safe_counter}")
