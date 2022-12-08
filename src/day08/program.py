

with open("./data.txt", "r") as f:
    data = f.read()
f.close()

forest = data.splitlines()
height = len(forest)
width = len(forest[0])

def viewScore(x,y):

    candidate = forest[y][x]
    topCount = 0
    bottomCount = 0
    rightCount = 0
    leftCount = 0
    # check to top
    for checky in range(y-1, -1, -1):
        topCount += 1
        if candidate <= forest[checky][x]: break

    # check bottom
    for checky in range(y+1, height):
        bottomCount += 1
        if candidate <= forest[checky][x]: break

    # check left
    for checkx in range(x-1, -1, -1):
        leftCount += 1
        if candidate <= forest[y][checkx]: break

    # check right
    for checkx in range(x+1, width):
        rightCount += 1
        if candidate <= forest[y][checkx]: break

    return topCount * bottomCount * leftCount * rightCount

def tallenough(x,y):

    if (x == 0) or (x == (width-1)) or (y == 0) or (y == (height - 1)):
        return True

    candidate = forest[y][x]

    top = True
    bottom = True
    left = True
    right = True

    # check to top
    for checky in range(0,y):
        if candidate <= forest[checky][x]: 
            top = False
            break

    # check bottom
    for checky in range(y+1, height):
        if candidate <= forest[checky][x]: 
            bottom = False
            break

    # check left
    for checkx in range(0, x):
        if candidate <= forest[y][checkx]: 
            left = False
            break

    # check right
    for checkx in range(x+1, width):
        if candidate <= forest[y][checkx]: 
            right = False
            break

    return top or bottom or left or right

p1 = 0
p2 = 0
for y in range(0, width):
    for x in range(0, height):
        if tallenough(x,y): p1 += 1

        score = viewScore(x,y)
        if score > p2: p2 = score

print("p1: {p1} (1789)".format(p1 = p1))
print("p2: {p2} (314820)".format(p2 = p2))