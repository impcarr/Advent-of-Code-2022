from itertools import zip_longest
def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

sacks = open("input.txt", "r").read().splitlines()
total = 0
for s1, s2, s3 in grouper(3,sacks):
    s1, s2, s3 = set(s1), set(s2), set(s3)    
    res = set.intersection(s1,s2,s3).pop()
    if res.isupper():
        total += ord(res)-ord("A")+27
    else:
        total += ord(res)-ord("a")+1
    
print(total)