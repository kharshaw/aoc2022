from functools import reduce

with open("./data.txt","r") as f:
    data = f.read()
f.close()

def movetail(head, tail, rope):
    
    knot = 0
    dx = rope[head]["x"] - rope[tail]["x"]
    dy = rope[head]["y"] - rope[tail]["y"]
    #print("head at x:{x} y:{y}".format(x=hx,y=hy))
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
        rope.append({"x": 0, "y": 0, "visits": set("[0:0]")})
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

print("p1: {p1}".format(p1 = reduce(lambda acc, val: acc + len(val["visits"]), rope1)))



