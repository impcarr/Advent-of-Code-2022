points = {"X":1, "Y":2, "Z":3, "W":6, "D":3, "L":0}

calc = {"X":0b100, "Y":0b101, "Z":0b110, "A":0b000, "B":0b001, "C":0b010}

def get_score(moves):
    m2,m1 = moves.split()
    res = calc[m1] - calc[m2]
    score = 0
    if res == 4:
        score += points["D"]
    elif res % 3 == 0:
        score += points["L"]
    else:
        score += points["W"]
    score += points[m1]
    return score

moves = open("input.txt", "r").read().splitlines()
total = 0
for move in moves:
    total += get_score(move)
print(total)
