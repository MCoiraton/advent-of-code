txt_input = open("day four\input.txt","r")
pairs=txt_input.readlines()
r=0
for pair in pairs:
    e1, e2 = pair.split(",")
    start1, end1 = map(int, e1.split("-"))
    start2, end2 = map(int, e2.split("-"))
    if (start1 <= start2 and end2<= end1) or (start2 <= start1 and end1 <= end2):
        r += 1

print(r)