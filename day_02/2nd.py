moves = {"A": "rock", "B": "paper", "C": "scissors"}
win_moves = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
lose_moves = {v: k for k, v in win_moves.items()}

def check_score(move):
    enemy, result = move.split(" ")
    score = 0
    if result == "X": # Lose
        player = win_moves[moves[enemy]]
    elif result == "Y": # Draw
        player = moves[enemy]
        score += 3
    elif result == "Z": # Win
        player = lose_moves[moves[enemy]]
        score += 6
    return score + list(win_moves.keys()).index(player) + 1

with open("input", "r") as fp:
    moves_arr = fp.read().strip().split("\n")
 
print(sum(map(check_score, moves_arr)))
