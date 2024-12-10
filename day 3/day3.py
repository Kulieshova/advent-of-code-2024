import re
data_file = open("data.txt", "r")


# Part 1
valid_sum = 0
for line in data_file.readlines():
    valid_inputs = re.findall(r"mul\(([0-9]+),([0-9]+)\)", line)
    for valid_input in valid_inputs:
        valid_sum += int(valid_input[0]) * int(valid_input[1])

print(f"The sum of valid muls is: {valid_sum}")
    