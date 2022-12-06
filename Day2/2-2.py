nest_loss = {"A":3, "B":1, "C":2}
nest_draw = {"A":4, "B":5, "C":6}
nest_win = {"A":8, "B":9, "C":7}
point_nest = {"X":nest_loss, "Y":nest_draw, "Z":nest_win}

calc = {"X":0b100, "Y":0b101, "Z":0b110, "A":0b000, "B":0b001, "C":0b010}

def get_score(moves):
    move,result = moves.split()
    return point_nest[result][move]

moves = open("input.txt", "r").read().splitlines()
total = 0
for move in moves:
    total += get_score(move)
print(total)
