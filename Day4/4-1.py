assignments = open("input.txt", "r").read().splitlines()

total = 0
for assignment in assignments:
    elf1, elf2 = assignment.split(',')
    min1, max1 = map(int, elf1.split('-'))
    min2, max2 = map(int, elf2.split('-'))
    if (min1 <= min2 and max1 >= max2):
        total+=1
    elif (min1 >= min2 and max1 <= max2):
        total+=1

print(total)