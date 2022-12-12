with open("./data.txt", "r") as f:
    data = f.read()
f.close()

def processCycle(cycle):
    #print("    process cycle {c}".format(c=cycle))
    return cycle == 20 or (cycle - 20) % 40 == 0

def initdisplay():
    return [
        "........................................",
        "........................................",
        "........................................",
        "........................................",
        "........................................",
        "........................................"
    ]
def showdisplay(display):
    for i in range(0,len(display)):
        print(display[i])

def setPixel(cycle, X, display):
    y = cycle // 40
    x = cycle % 40
    row = display[y]
    sprite = range(X-1,X+2)

    char = "."
    if (x in sprite):
        char = "#"
    
        newrow = list(row)
        newrow[x] = char
        display[y] = "".join(newrow)
        
def completecycle(cycles, x, addend):
    pass
    
X = 1
addend = 0
cycle = 0
totalSignalStrength = 0
opcycle = 1
display = initdisplay()

for line in data.splitlines():
    done = False
    opcycle = 1

    op = line[:4]
    while not done:
        if op == "noop":
            done = True
            X += addend
            addend = 0
        elif op == "addx":
            if opcycle == 1:
                X += addend 
                done = False
                opcycle = 2
                
            elif opcycle == 2:
                addend = int((line.split())[1])
                done = True

        setPixel(cycle, X, display)

        cycle += 1

        if processCycle(cycle):
            totalSignalStrength += cycle * X
            print("cycle:{c} X: {x} strength: {s}".format(c = cycle, x = X, s = cycle * X))  

X += addend 

if processCycle(cycle):
    totalSignalStrength += cycle * X
    print("cycle:{c} X: {x} strength: {s}".format(c = cycle, x = X, s = cycle * X))  
              
        
print("p1: {s}".format(s = totalSignalStrength))

showdisplay(display)
