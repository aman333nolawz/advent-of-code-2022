import string

def priority(l): return string.ascii_letters.index(l) + 1

def find_badge(rucksacks):
    r1, r2, r3 = rucksacks
    for item in r1:
        if item in r2 and item in r3:
            return priority(item)

with open("input", "r") as fp:
    racksacks = fp.read().strip().split("\n")

racksacks = [[racksacks[i], racksacks[i+1], racksacks[i+2]] for i in range(0, len(racksacks), 3)]
print(sum(map(find_badge, racksacks)))
