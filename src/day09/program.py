from functools import reduce

with open("./data.txt","r") as f:
    data = f.read()
f.close()

def movetail(head, tail, rope):
    if (head == len(rope)-1): return
    knot = 0
    dx = rope[head]["x"] - rope[tail]["x"]
    dy = rope[head]["y"] - rope[tail]["y"]
    
    if tail < len(rope):
        while abs(dx) > 1 or abs(dy) > 1:

            if (dx != 0 and dy != 0):
                rope[tail]["x"] += dx//abs(dx)
                rope[tail]["y"] += dy//abs(dy)
            elif (dx != 0):
                rope[tail]["x"] += dx//2
            elif (dy !=0):
                rope[tail]["y"] += dy//2
        
            rope[tail]["visits"].add("{x}:{y}".format(x=rope[tail]["x"],y=rope[tail]["y"]))
            
            dx = rope[head]["x"] - rope[tail]["x"]
            dy = rope[head]["y"] - rope[tail]["y"]

    movetail(head+1, tail+1, rope)    

def initializeRope(knotCount):
    rope = []

    for i in range(0,knotCount):
        visits = set()
        visits.add("0:0")        
        rope.append({"x": 0, "y": 0, "visits": visits})
    return rope

def move(rope, moves):
    for move in moves:
        
        (direction, distance) = move.split(" ")

        for d in range(0,int(distance)):

            if direction == "R":
                rope[0]["x"] += 1
            elif direction == "L":
                rope[0]["x"] -= 1
            elif direction == "U":
                rope[0]["y"] += 1
            elif direction == "D":
                rope[0]["y"] -= 1

            movetail(0, 1, rope)


moves = data.splitlines()

rope1 = initializeRope(2)
move(rope1, moves)
print("p1: {p1}".format(p1 = reduce(lambda acc, val: acc + len(val["visits"]), rope1[1:],0)))


rope2 = initializeRope(10)
move(rope2, moves)
print("p2: {p2}".format(p2 = len(rope2[-1]["visits"])))



