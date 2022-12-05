from functools import reduce

with open ("./data.txt","r") as f:
    pair = f.read().splitlines()

f.close()

pairs = []

containments = 0
overlaps = 0

for p in pair:
    assign1, assign2 = [[int(j) for j in i] for i in [x.split("-") for x in p.split(",")]]


    if ((assign1[0] >= assign2[0] and assign1[1] <= assign2[1]) and
        (assign2[0] >= assign1[0] and assign2[1] <= assign1[1])):
        containments += 1
        overlaps += 1
    elif ((assign1[0] >= assign2[0] and assign1[0] <= assign2[1]) or
        (assign2[0] >= assign1[0] and assign2[0] <= assign1[1])):
        overlaps += 1
    
    # area1 = set(range(assign1[0], assign1[1]+1))
    # area2 = set(range(assign2[0], assign2[1]+1))



    # if area1.issubset(area2) or area1.issuperset(area2):
    #     containments += 1
    #     overlaps += 1
    # elif not area1.isdisjoint(area2):
    #     overlaps += 1

print("p1: " + str(containments))

print("p2: " + str(overlaps))
