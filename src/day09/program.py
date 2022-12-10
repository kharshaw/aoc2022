from math import dist

with open("./data.txt","r") as f:
    data = f.read()
f.close()

def movetail(hx, hy, tx, ty, direction, visits):
    
    dx = hx - tx
    dy = hy - ty
    #print("head at x:{x} y:{y}".format(x=hx,y=hy))
    while abs(dx) > 1 or abs(dy) > 1:

        if (dx != 0 and dy != 0):
            tx += dx//abs(dx)
            ty += dy//abs(dy)
        elif (dx != 0):
            tx += dx//2
        elif (dy !=0):
            ty += dy//2
    
        #print ("move tail to x:{tx} y:{ty}".format(tx=tx,ty=ty))
        visits.add("{x}:{y}".format(x=tx,y=ty))
        
        dx = hx - tx
        dy = hy - ty
        
    return (tx,ty)

moves = data.splitlines()
tx = 0
ty = 0

hx = 0
hy = 0

visits = set(["0:0"])

for move in moves:
       
    (direction, distance) = move.split(" ")

    #print(direction, distance)
   
    for d in range(0,int(distance)):

        if direction == "R":
            hx += 1
        elif direction == "L":
            hx -= 1
        elif direction == "U":
            hy += 1
        elif direction == "D":
            hy -= 1

        (tx,ty) = movetail(hx, hy, tx,ty, direction, visits)

    #print(sorted(visits))


print(len(visits))


