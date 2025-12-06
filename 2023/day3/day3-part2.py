input_file = open("input.txt", "r")
# input_file = open("example_input.txt", "r")

symbol_list = ["*"]
gear_adjacent_numbers = []
gear_locations = []
line_data = input_file.readlines()

def logGearLocation(line, index):
    gear_locations.append([line,index])
    
def checkForAdjacentOrDiagonalSymbol(current_line_number, start_index, end_index):
    adjacent_and_diagnonal_chars = []
    current_line_data = line_data[current_line_number].strip()
    left_adjacent = None
    right_adjacent = None

    if start_index != 0:
        left_adjacent = current_line_data[start_index-1]
        adjacent_and_diagnonal_chars.append(left_adjacent)
        if left_adjacent in symbol_list:
            logGearLocation(current_line_number, start_index-1)
    
    if end_index != (len(current_line_data)-1):
        right_adjacent = current_line_data[end_index+1]
        adjacent_and_diagnonal_chars.append(right_adjacent)
        if right_adjacent in symbol_list:
            logGearLocation(current_line_number, end_index+1)
 
    
    if current_line_number != 0:
        previous_line = line_data[current_line_number-1].strip()
        for index, char in enumerate(previous_line):
            if (index >= start_index-1) and (index <= end_index+1):
                adjacent_and_diagnonal_chars.append(char)
                if char in symbol_list:
                    logGearLocation(current_line_number-1, index)
                

    if current_line_number != (len(line_data)-1):
        next_line = line_data[current_line_number+1].strip()
        for index, char in enumerate(next_line):
            if (index >= start_index-1) and (index <= end_index+1):
                adjacent_and_diagnonal_chars.append(char)
                if char in symbol_list:
                    logGearLocation(current_line_number+1, index)

    for entry in adjacent_and_diagnonal_chars:
        if entry in symbol_list:
            return True

    return False

for line_number,line_content in enumerate(line_data):
    current_number = []
    building_number = False
    number_start_index = 0
    start_index_logged = False
    number_end_index = 0
    for index, c in enumerate(line_content):
        if c.isdigit():
            building_number = True
            if not start_index_logged:
                start_index_logged = True
                number_start_index = index
            current_number.append(c)
        elif not c.isdigit() and building_number:
            # check for adjacent or diagonal symbol
            # if adjacent or diagonal symbol is present, add to valid_engine_numbers
            building_number = False
            start_index_logged = False
            number_end_index = index-1
            if checkForAdjacentOrDiagonalSymbol(line_number, number_start_index, number_end_index):
                gear_adjacent_numbers.append(''.join(current_number))
            current_number = []

counter = 0
matched_entries = []
for i in range(len(gear_locations)):
    for j in range(i+1, (len(gear_locations))):
        if gear_locations[i] == gear_locations[j]:
            counter += 1
            saved = gear_adjacent_numbers[j]         
    if counter == 1:
        counter = 0
        matched_entries.append([gear_adjacent_numbers[i], saved])

products = []
sum_of_products = 0
for entry in matched_entries:
    sum_of_products += int(entry[0]) * int(entry[1])

print(f"Gear locations: {gear_locations}")
print(f"Gear adjacent numbers: {gear_adjacent_numbers}")


print("==========================================")
print("==========================================")
print(f"Sum of gear ratios: {sum_of_products}")
print("==========================================")
print("==========================================")