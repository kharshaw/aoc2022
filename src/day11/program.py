from functools import reduce

with open("./data.txt","r") as f:
    data = f.read()
f.close()


def initMonkey(monkey: str, monkeys: dict):
    l = monkey.splitlines()
    id = int(l[0][7:len(l[0])-1])
    items = [int(i) for i in l[1][17:].split(", ")]
    op, oparg = l[2][23:].split(" ")
    testdiv = int(l[3][20:])
    testt = int(l[4][28:])
    testf = int(l[5][29:])

    monkeys[id] = {
        "id": id,
        "items": items,
        "op": op,
        "oparg": oparg,
        "testdiv": testdiv,
        True: testt,
        False: testf,
        "compares": 0
    }

def keepaway(monkeys, rounds, worry):
    for round in range(0,rounds):
        for key in monkeys.keys():
            monkey = monkeys[key]

            #print("monkey {id}".format(id = monkey["id"]))
            for item in monkey["items"]:
                factor: int
                if monkey["oparg"] == "old":
                    factor = item
                else:
                    factor = int(monkey["oparg"])

                newitem = 0
                if monkey["op"] == "*":
                    newitem = item * factor 
                elif monkey["op"] == "+":
                    newitem = item + factor

                if worry == 1:
                    newitem //= 3
                else:
                    newitem %= worry

                monkey["compares"] += 1

                passto = monkey[newitem % monkey["testdiv"] == 0]

                # print("  throws {i} to monkey {p} as {n}".format(i = item, p=passto,n=newitem))
                
                monkeys[passto]["items"].append(newitem)

            monkey["items"].clear()
        # if round % 100 == 0: print("Done round {r}".format(r=round))

    return monkeys


def parsemonkedata(monkeydata):
    monkeys = {}
    for monkey in monkeydata:
        initMonkey(monkey, monkeys)
    return monkeys

def getresult(monkeys):
    mc = list(map(lambda m: m["compares"],monkeys.values()))
    mc.sort(reverse=True)
    return mc[0] * mc[1]

monkeydata = data.split("\n\n")

monkeys = parsemonkedata(monkeydata)
monkeys = keepaway(monkeys,20,1)

p1 = getresult(monkeys)
print("p1: {t}".format(t=p1))

monkeys.clear()
monkeys = parsemonkedata(monkeydata)

factor = 1
for m in monkeys.values():
    factor *= m["testdiv"]

monkeys = keepaway(monkeys,10000,factor)

p2 = getresult(monkeys)
print("p2: {t}".format(t=p2))
