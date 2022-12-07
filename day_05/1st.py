def create_stacks(inp):
    inp = inp.split("\n")[:-1]
    stacks = {i: [] for i in range(1, 10)}
    for i, line in enumerate(inp, 1):
        for c in range(0, len(line), 4):
            crate = line[c:c+3]
            if crate.strip():
                stacks[c//4+1].insert(0, crate.replace("[", "").replace("]", ""))
    return stacks

def parse_instructions(inp, stacks):
    inp = inp.split("\n")
    for instruction in inp:
        move, _from, to = [int(i) for i in instruction.split(" ")[1::2]]
        for i in range(move):
            stacks[to].append(stacks[_from].pop())

def create_message(stacks):
    msg = ""
    for k in stacks:
        msg += stacks[k][-1]
    print(msg)
            
with open("input", "r") as fp:
    inp = fp.read().rstrip()

crates, instructions = inp.split("\n\n")
stacks = create_stacks(crates)
parse_instructions(instructions, stacks)
print(create_message(stacks))

