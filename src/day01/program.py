from functools import reduce

with open("./data.txt", "r") as f:

    elf = 1
    cal = 0
    elves = []

    for line in f:
        data = line.strip()

        if data == "":
            # new elf
            elves.append([elf, cal])
            cal = 0
            elf += 1
        else:
            # add to existing elf
            cal += int(data)

    elves.append((elf, cal))


f.close()

elves.sort(key=lambda e: e[1], reverse=True)


print("The elf with the most calories is {bigElf} with {totalCalories}, should be 74394".format(bigElf = elves[0][0], totalCalories = elves[0][1]))

top3 = reduce(lambda acc, val: val[1] + acc, elves[slice(3)], 0)

print("The top three elves have {cal} calories, should be 212836".format(cal = top3))