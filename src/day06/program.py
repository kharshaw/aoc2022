

with open("./data.txt",) as f:
    data = f.read()

f.close()


def findCode(data, length):
    buffer = list()

    for idx, c in enumerate(data, 1):
        if c in buffer:
            while True:
                f = buffer[0]
                buffer.pop(0)
                if f == c: break
            
        buffer.append(c)
        if len(buffer) == length: 
            break

    return (idx, "".join(buffer))

print(findCode("bvwbjplbgvbhsrlpgdmjqwftvncz",4)) # 5
print(findCode("nppdvjthqldpwncqszvftbrmjlhg",4)) # 6
print(findCode("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",4)) # 10
print(findCode("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",4)) # 11

print(findCode(data,4))

print(findCode("bvwbjplbgvbhsrlpgdmjqwftvncz",14)) # 5
print(findCode("nppdvjthqldpwncqszvftbrmjlhg",14)) # 6
print(findCode("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",14)) # 10
print(findCode("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",14)) # 11

print(findCode(data,14))

