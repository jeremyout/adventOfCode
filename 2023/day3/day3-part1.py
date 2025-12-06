input_file = open("input.txt", "r")
# input_file = open("example_input.txt", "r")

symbol_list = ["!", "@", "#", "$", "%", "^", "&", "(", ")", "*", "-", "+", "=", "/"]
symbol_index_to_process = []
valid_engine_numbers = []
line_data = input_file.readlines()
    
def checkForAdjacentOrDiagonalSymbol(current_line_number, start_index, end_index):
    adjacent_and_diagnonal_chars = []
    current_line_data = line_data[current_line_number].strip()
    left_adjacent = None
    right_adjacent = None

    if start_index != 0:
        left_adjacent = current_line_data[start_index-1]
        adjacent_and_diagnonal_chars.append(left_adjacent)
    
    if end_index != (len(current_line_data)-1):
        right_adjacent = current_line_data[end_index+1]
        adjacent_and_diagnonal_chars.append(right_adjacent)
    
    if current_line_number != 0:
        previous_line = line_data[current_line_number-1].strip()
        for index, char in enumerate(previous_line):
            if (index >= start_index-1) and (index <= end_index+1):
                adjacent_and_diagnonal_chars.append(char)

    if current_line_number != (len(line_data)-1):
        next_line = line_data[current_line_number+1].strip()
        for index, char in enumerate(next_line):
            if (index >= start_index-1) and (index <= end_index+1):
                adjacent_and_diagnonal_chars.append(char)

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
                valid_engine_numbers.append(''.join(current_number))
            current_number = []

sum = 0
for num in valid_engine_numbers:
    sum += int(num)

print("==========================================")
print("==========================================")
print(f"Sum of valid engine numbers: {sum}")
print("==========================================")
print("==========================================")