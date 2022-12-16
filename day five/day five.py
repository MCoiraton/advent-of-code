txt_input=open("day five\input.txt","r")
procedures=[]
stacks=[
    ["J","Z","G","V","T","D","B","N"],
    ["F","P","W","D","M","R","S"],
    ["Z","S","R","C","V"],
    ["G","H","P","Z","J","T","R"],
    ["F","Q","Z","D","N","J","C","T"],
    ["M","F","S","G","W","P","V","N"],
    ["Q","P","B","V","C","G"],
    ["N","P","B","Z"],
    ["J","P","W"],
]
i=1
for lines in txt_input.readlines():
    if i>=11 :
        procedures.append(lines)
    i+=1
for procedure in procedures:
    nbs=int(procedure.split(" from ")[0].strip().split(" ")[-1])
    fr=int(procedure.split(" from ")[1].split(" to ")[0].strip())
    to=int(procedure.split(" from ")[1].split(" to ")[1].strip())
    for j in range(0,nbs):
        if(len(stacks[fr-1])>0):
            stacks[to-1].insert(0,stacks[fr-1].pop(0))

#affichage :
r=""
for stack in stacks:
    print(str(stack[0]))
    r+=stack[0]
print(r)