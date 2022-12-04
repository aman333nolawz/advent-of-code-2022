with open("input", "r") as fp:
    calories = fp.read().strip().split("\n\n")

def max_3(l):
    r = [0, 0, 0]
    for num in l:
        if num > min(r):
            r[r.index(min(r))] = num
    return r

def sum_of_calories(n):
    return sum(int(i) for i in n.split("\n"))

print(sum(max_3(map(sum_of_calories, calories))))
