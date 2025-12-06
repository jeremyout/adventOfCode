input_file = open("input.txt", "r")

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
extracted_numbers = []

for line in (input_file):
    first_digit = ""
    last_digit = ""
    for char in line:
        if char in digits:
            if not first_digit:
                first_digit = char
            last_digit = char
    extracted_numbers.append(first_digit+last_digit)

sum = 0
for num in extracted_numbers:
    sum += int(num)

print(sum)

input_file.close()