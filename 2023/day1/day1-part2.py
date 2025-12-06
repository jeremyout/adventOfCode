input_file = open("input.txt", "r")
# input_file = open("example_input_p2.txt", "r")

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
word_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
extracted_numbers = []


for line in (input_file):
    first_digit = ""
    last_digit = ""
    for i in range(len(line)):
        if line[i] in digits:
            if not first_digit:
                first_digit = line[i]
            last_digit = line[i]
        else:
            for key in word_digits.keys():
                if (key in line) and (key[0] == line[i]) and (key[1] == line[i+1]) and (key[2] == line[i+2]):
                    if not first_digit:
                        first_digit = word_digits[key]
                    last_digit = word_digits[key]
    extracted_numbers.append(first_digit+last_digit)

sum = 0
for num in extracted_numbers:
    sum += int(num)

print(sum)

input_file.close()