from functools import reduce
import re

with open ("./data.txt","r") as f:
    data = f.read().splitlines()

f.close()

labelRe = re.compile("\s*\d\s*")
moveRe = re.compile("\d+")
crateRe = re.compile("[A-Z]")

section = 0
stacks = []
crateData = []
moves = list([])
for line in data:
    if section == 0:
        if labelRe.match(line):
            section = 1
            for s in labelRe.findall(line):
                stacks.append([])
        else:
            crates = [line[i:i+4] for i in range(0, len(line), 4)]
            crateData.append(crates)
    elif section == 1:
        if len(line) == 0:
            section = 2
    elif section == 2:
        (count, orig, dest) = moveRe.findall(line)
        moves.append([int(count), int(orig), int(dest)])

for c in crateData:
    x = 0
    for x in range(len(c)):
        crate = crateRe.findall(c[x])
        if len(crate) == 1:
            stacks[x].append(crate[0])

print(stacks)

print(moves)

for m in moves:
    print(m)
    for n in range(m[0]):
        
        crate = stacks[m[1]-1][0]
        stacks[m[2]-1].insert(n, crate)
        stacks[m[1]-1].remove(crate)


print(stacks)


code = ""
for s in stacks:
    code += s[0]


print(code)

