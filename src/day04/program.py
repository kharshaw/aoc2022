from functools import reduce

with open ("./data.txt","r") as f:
    pair = f.read().splitlines()

f.close()

pairs = []

containments = 0
overlaps = 0

for p in pair:
    elves = p.split(",")

    elf1, elf2 = elves[0], elves[1]
    assign1 = (int(elf1.split("-")[0]), int(elf1.split("-")[1]))
    assign2 = (int(elf2.split("-")[0]), int(elf2.split("-")[1]))

    if (assign1[0] >= assign2[0] and assign1[1] <= assign2[1] or 
        assign2[0] >= assign1[0] and assign2[1] <= assign1[1]):
        containments += 1
        overlaps += 1
    elif (assign1[1] in range(assign2[0], assign2[1]+1) or 
        assign1[0] in range(assign2[0], assign2[1]+1)):
        overlaps += 1

print("p1: " + str(containments))

print("p2: " + str(overlaps))
