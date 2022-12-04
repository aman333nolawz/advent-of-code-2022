import string

def priority(l): return string.ascii_letters.index(l) + 1

def check_duplicate(rucksack):
    first_comp = rucksack[:len(rucksack)//2]
    second_comp = rucksack[len(rucksack)//2:]
    for item in first_comp:
        if item in second_comp: return priority(item)


with open("input", "r") as fp:
    racksacks = fp.read().strip().split("\n")
print(sum(map(check_duplicate, racksacks)))
