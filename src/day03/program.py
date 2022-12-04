from functools import reduce

with open ("./data.txt","r") as f:
    sacks = f.read().splitlines()

f.close()


def splitCompartments(sack):
    size = len(sack)
    compartment1, compartment2 = sack[:size//2], sack[size//2:]
    return (compartment1, compartment2)

def findCommonItems(compartments):
    common = []
    for c1 in list(compartments[0]):
        if c1 in list(compartments[1]):
            if c1 not in common:
                common.append(c1)
    
    return common

def priority(item):
    if item.isupper():
        p = 27 + ord(item) - ord("A")
    else:
        p = 1 + ord(item) - ord("a")

    return p


# part 1
total = 0
for sack in sacks:
    compartments = splitCompartments(sack)
    items = findCommonItems(compartments)

    for c in items:
        total += priority(c)

print("part1(8018): " + str(total))

def findBadge(sack1, sack2, sack3):
    for i in list(sack1):
        if i in list(sack2) and i in list(sack3):
            return i

r = 0
badges = []
while r < len(sacks):
    badge = findBadge(sacks[r], sacks[r+1], sacks[r+2])
    badges.append(badge)
    r += 3

total = 0
for b in badges:
    total += priority(b)

print("part2(2518): " + str(total))