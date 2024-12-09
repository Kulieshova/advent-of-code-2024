data_file = open("data.txt", "r")
list1 = []
list2 = []
distance = 0

for line in data_file.readlines():
    entry = line.split()
    list1.append(int(entry[0]))
    list2.append(int(entry[1]))

list1.sort()
list2.sort()

for i in range(len(list1)):
    distance += abs(list1[i] - list2[i])

print(f"The total distance between two lists is {distance}")