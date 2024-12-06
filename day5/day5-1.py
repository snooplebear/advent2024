from collections import defaultdict

# Read the file
with open("day5_input.txt", "r") as file:
    content = file.read().split("\n\n")
    page_rules_section = content[0]
    book_section = content[1]

pair_dict = defaultdict(list)
for line in page_rules_section.splitlines():
    left, right = map(int, line.split('|'))
    pair_dict[right].append(left)

lists = []
for line in book_section.splitlines():
    values = list(map(int, line.split(',')))
    lists.append(values)

print("\nANSWER")

final_lists=[]

final_count = 0

for lst in lists[:]:
    print(f"Processing list: {lst}")
    valid = True

    temp_list = list(lst)
    while temp_list:
        page = temp_list.pop(0)
        print()
        print(f"Checking page: {page}")
        
        if any(value in temp_list for value in pair_dict[page]):
            valid = False
            break
        # else valid
            
        if not temp_list and valid:
            middle_value = lst[len(lst)//2]
            print(lst)
            print(f'middle value is {middle_value}')
            final_count += middle_value

print(final_count)