moves = {"A": "rock", "B": "paper", "C": "scissors", "X": "rock", "Y": "paper", "Z": "scissors"}
win_moves = {"rock": ["scissors"], "paper": ["rock"], "scissors": ["paper"]}

def check_win(mov1, mov2):
    if moves[mov1] == moves[mov2]: return 3
    if win_moves[moves[mov1]][0] == moves[mov2]: return 6
    return 0

def check_score(move):
    enemy, player = move.split(" ")
    player_score = check_win(player, enemy)
    return player_score + list(win_moves.keys()).index(moves[player]) + 1

with open("input", "r") as fp:
    moves_arr = fp.read().strip().split("\n")
 

print(sum(map(check_score, moves_arr)))
