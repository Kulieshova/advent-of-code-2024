data_file = open("data.txt", "r")
list1 = []
list2 = []

for line in data_file.readlines():
    entry = line.split()
    list1.append(int(entry[0]))
    list2.append(int(entry[1]))

list1.sort()
list2.sort()

# PART 1
distance = 0
for i in range(len(list1)):
    distance += abs(list1[i] - list2[i])

print(f"The total distance between two lists is {distance}")


# PART 2
similarity = 0
left_set = set(list1)
frequency_list2 = {}

for number in list2:
    frequency_list2[number] = frequency_list2.get(number, 0) + 1

for number in left_set:
    if number in frequency_list2:
        similarity += number * frequency_list2[number]

print(f"The similarity score for the lists is {similarity}")
