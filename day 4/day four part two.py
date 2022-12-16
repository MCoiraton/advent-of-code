txt_input = open("day 4\input.txt","r")
pairs=txt_input.readlines()
r=0
for pair in pairs:
    e1, e2 = pair.split(",")
    start1, end1 = map(int, e1.split("-"))
    start2, end2 = map(int, e2.split("-"))
    if any(x in range(start2, end2+1) for x in range(start1, end1+1)) or any(x in range(start1, end1+1) for x in range(start2, end2+1)):
        r += 1

print(r)