with open("input.txt", "r") as f:
    lines = f.readlines()

max = 0
curr = 0
for line in lines:
    try:
        curr += int(line)
    except ValueError:
        if curr > max:
            max = curr
        curr = 0
print(max)

