from functools import reduce
import re
import copy
import math

with open ("./data.txt","r") as f:
    data = f.read().splitlines()

f.close()


def initialize2():
    with open ("./data.txt","r") as f:
        data = f.read()
    f.close()

    moves = []
    pack, instr = data.split("\n\n")

    # get packing layout
    for idx, pl in enumerate(pack.splitlines()):
        if idx == 0:  stacks = [list() for i in range(math.ceil(len(pl)/4))]

        for idx, loc in enumerate(range(1, len(pl), 4)):
            if (pl[loc] != " " and not pl[loc].isdigit()): stacks[idx].append(pl[loc])

    for il in instr.splitlines():
        (count, orig, dest) = re.findall("\d+", il)
        moves.append([int(count), int(orig), int(dest)])

    return (stacks, moves)

# def initialize(data):
#     labelRe = re.compile("\s*\d\s*")
#     moveRe = re.compile("\d+")
#     crateRe = re.compile("[A-Z]")

#     section = 0
#     stacks = []
#     crateData = []
#     moves = list([])

#     for line in data:
#         if section == 0:
#             if labelRe.match(line):
#                 section = 1
#                 for s in labelRe.findall(line):
#                     stacks.append([])
#             else:
#                 crates = [line[i:i+4] for i in range(0, len(line), 4)]
#                 crateData.append(crates)
#         elif section == 1:
#             if len(line) == 0:
#                 section = 2
#         elif section == 2:
#             (count, orig, dest) = moveRe.findall(line)
#             moves.append([int(count), int(orig), int(dest)])

#     for c in crateData:
#         x = 0
#         for x in range(len(c)):
#             crate = crateRe.findall(c[x])
#             if len(crate) == 1:
#                 stacks[x].append(crate[0])

#     return (stacks, moves)

def moveEm9000(stacks, moves):
    s = copy.deepcopy(stacks)

    for m in moves:
        for n in range(m[0]):
            
            crate = s[m[1]-1][0]
            s[m[2]-1].insert(0, crate)
            s[m[1]-1].remove(crate)
    return s

def moveEm9001(stacks, moves):
    s = copy.deepcopy(stacks)
    for m in moves:
        for n in range(m[0]):
            
            crate = s[m[1]-1][0]
            s[m[2]-1].insert(n, crate)
            s[m[1]-1].remove(crate)
    return s

def getCode(stacks):
    code = ""
    for s in stacks:
        code += s[0]
    return code

# (stacks, moves) = initialize(data)
(stacks, moves) = initialize2()

print("part 1 code: {c}".format(c = getCode(moveEm9000(stacks, moves))))

print("part 2 code: {c}".format(c = getCode(moveEm9001(stacks, moves))))

