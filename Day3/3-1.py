from itertools import count
sacks = open("input.txt", "r").read().splitlines()
total = 0
for sack in sacks:
    s1, s2 = set(sack[:len(sack)//2]), set(sack[len(sack)//2:])
    res = set.intersection(s1,s2).pop()
    if res.isupper():
        total += ord(res)-ord("A")+27
    else:
        total += ord(res)-ord("a")+1
    
print(total)