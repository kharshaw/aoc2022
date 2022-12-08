with open("./data.txt",) as f:
    data = f.read()

f.close()

path = []
dirs = {}

def cd(dirName: str, path: list ):
    if dirName == "/": 
        path.clear()
        path.append("/")
    elif dirName == "..":
        if (len(path) > 0):
            path.pop()
    else:
        path.append(dirName)


def addfile(file, path: list):
    key = "/".join(path)
    bytes = int(file[0])
    size = 0

    p = path.copy()

    while len(p) > 0:
        key = "/".join(p)
        if key not in dirs.keys():
            dirs[key] = 0

        dirs[key] += bytes
        p.pop()
        
        

dirs["/"] = 0

for line in data.splitlines():
    if line[0] == "$":
        if line[2:4] == "cd":
            cd(line[5:], path)
    else:
        (a,b) = line.split(" ")
        if a.isnumeric():
            addfile((a,b), path)
        else:
            dirs["/".join(path) + "/" + b] = 0

total = 0
for f in dirs.items():
    if f[1] <= 100000:
        total += f[1]

print("p1: {t}".format(t = total))

bytes = list(dirs.values())
bytes.sort()

spaceused = dirs["/"]
target = 30000000 - (70000000 - spaceused)

for idx, b in enumerate(bytes):
    if b >= target:
        break

print("p2: {b}".format(b = b))


