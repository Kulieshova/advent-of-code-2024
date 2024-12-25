import re
data_file = open("data.txt", "r")
inputs = [line for line in data_file.readlines()]

# Part 1
valid_sum = 0
for line in inputs:
    valid_inputs = re.findall(r"mul\(([0-9]+),([0-9]+)\)", line)
    for valid_input in valid_inputs:
        valid_sum += int(valid_input[0]) * int(valid_input[1])

print(f"The sum of valid muls is: {valid_sum}")
    

# Part 2
modified_sum = 0
mul_enabled = True
command_pattern = r"(do\(\)|don't\(\)|mul\((\d{1,3}),\s*(\d{1,3})\))"

for line in inputs:
    valid_inputs_modified = re.findall(command_pattern, line)

    for input in valid_inputs_modified:
        if input[0] == "do()":
            mul_enabled = True
        elif input[0] == "don't()":
            mul_enabled = False
            
        if mul_enabled and input[0] != "do()":
            modified_sum += int(input[1]) * int(input[2])

print(f"The modified sum of valid muls is: {modified_sum}")
