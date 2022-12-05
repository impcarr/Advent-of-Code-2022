from collections import deque
from math import ceil
import re
start = open("startpos.txt").read().splitlines()
start.reverse()
boxes = [deque(["EMPTY"])]
for i in range(len(start[0].split())):
    boxes.append(deque())
for line in start:
    for i in range(len(line)):
        if(i % 4 == 1 and line[i] != " "):
            boxes[ceil(i/4)].append(line[i])
#print(boxes[1:])

moves = open("input.txt", "r").read().splitlines()
for move in moves:
    num, src, dest = map(int, re.findall(r'\d+', move))
    temp = deque()
    for i in range(num):
        temp.append(boxes[src].pop())
        
    for i in range(len(temp)):
        boxes[dest].append(temp.pop())
    #print(boxes[1:])
sub = ""
for box in boxes:
    sub += box.pop()
print(sub[5:])