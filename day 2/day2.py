data_file = open("data.txt", "r")

# PART 1
safe_reports = 0
max_change = 3
min_change = 1
for line in data_file.readlines():
    level = [int(x) for x in line.split()]
    is_increasing = level[0] < level[1]
    is_decreasing = level[0] > level[1]
    is_safe = True

    for i in range(len(level) - 1):
        if abs(level[i] - level[i + 1]) > max_change or abs(level[i] - level[i + 1]) < min_change:
            is_safe = False
            break
        elif is_decreasing and level[i] < level[i + 1]:
            is_safe = False
            break
        elif is_increasing and level[i] > level[i + 1]:
            is_safe = False
            break
    safe_reports += is_safe

print(f"The number of safe reports is {safe_reports}")