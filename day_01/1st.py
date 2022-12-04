with open("input", "r") as fp:
    calories = fp.read().strip().split("\n\n")

def sum_of_calories(n):
    return sum(int(i) for i in n.split("\n"))

print(max(map(sum_of_calories, calories)))
