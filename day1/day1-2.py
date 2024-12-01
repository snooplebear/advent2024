
list1 = []
list2 = []
try:
   with open("day_input.txt", "r") as day1_input:
      lines = day1_input.readlines()
   for line in lines:  
      numbers = line.split()
      list1.append(int(numbers[0]))
      list2.append(int(numbers[1]))
except FileNotFoundError:
    print("Error: The file 'day_input.txt' was not found.")
    exit(1)  # Exit the program if the file is not found

total = 0

for item in list1:
   occurrences = list2.count(item)
   total += occurrences * item

print(total)