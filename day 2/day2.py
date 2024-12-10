data_file = open("data.txt", "r")
max_change = 3
min_change = 1
levels = []

for line in data_file.readlines():
    level = [int(x) for x in line.split()]
    levels.append(level)

# PART 1
safe_reports = 0

def is_safe_simple(level):
    is_increasing = level[0] < level[1]
    is_decreasing = level[0] > level[1]
    is_safe = True

    for i in range(len(level) - 1):
        if not is_pair_safe(level[i], level[i+1], is_decreasing, is_increasing):
            is_safe = False
            break
    return is_safe

def is_pair_safe(a, b, is_decreasing, is_increasing):
    if abs(a - b) > max_change or abs(a - b) < min_change:
        return False
    elif is_decreasing and a < b:
        return False
    elif is_increasing and a > b:
        return False
    return True

for level in levels:
    safe_reports += is_safe_simple(level)

print(f"The number of safe reports is {safe_reports}")



# PART 2
def is_safe_problem_dampener(level):
    if is_safe_simple(level):
        return True
    else:
        i = 0
        while i < len(level):
            if is_safe_simple(level[:i] + level[i+1:]):
                return True
            i += 1
        return False  
    
safe_reports_problem_dampener = 0
for level in levels:
    safe_reports_problem_dampener += is_safe_problem_dampener(level)

print(f"The number of safe reports with problem dampener is {safe_reports_problem_dampener}")