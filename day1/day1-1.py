
list1 = []
list2 = []
with open("day_input.txt", "r") as day1_input:
	lines = day1_input.readlines()
for line in lines:  
   numbers = line.split()
   list1.append(int(numbers[0]))
   list2.append(int(numbers[1]))

list1.sort()
list2.sort()

difference = [abs(a - b) for a, b in zip(list1, list2)]

print(sum(difference))
