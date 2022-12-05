def check_overlap(pair):
    r1, r2 = pair.split(",")
    r1_1, r1_2 = [int(i) for i in r1.split("-")]
    r2_1, r2_2 = [int(i) for i in r2.split("-")]
    r1 = range(r1_1, r1_2+1)
    r2 = range(r2_1, r2_2+1)
    return any(i in r1 for i in r2) or any(i in r2 for i in r1)

with open("input", "r") as fp:
    ids = fp.read().strip().split("\n")

print(sum(map(check_overlap, ids)))
