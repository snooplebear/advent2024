import re

with open("day3_input.txt", "r") as input_file:
    lines = input_file.read()

pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
matches = pattern.findall(lines)

final_answer = 0
for match in matches:
    temp_multiplier = 1
    numbers = re.findall(r'\d+', match)
    for number in numbers:
        temp_multiplier *= int(number)

    final_answer += temp_multiplier

print(final_answer)