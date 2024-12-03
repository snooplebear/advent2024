import re

with open("day3_input.txt", "r") as input_file:
    lines = input_file.read()

pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)")

matches = re.findall(pattern, lines)

final_answer = 0
enabled = True

for match in matches:
    if "mul" in match and enabled:
        temp_multiplier = 1
        numbers = re.findall(r'\d+', match)
        for number in numbers:
            temp_multiplier *= int(number)
        final_answer += temp_multiplier
        print(numbers)
    else:
        if "don't()" in match:
            enabled = False
        elif "do()" in match:
            enabled = True

print("Final Answer:", final_answer)
