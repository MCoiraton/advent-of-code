
max_calories=0
elf=0
txt_input = open("input.txt","r")

tbl_input=txt_input.read().split("\n\n")
print(tbl_input)
for i in range(0,len(tbl_input)):
    calories = sum(map(int,tbl_input[i].split("\n")))
    if calories>max_calories :
        max_calories=calories
        elf=i

print("Elf="+str(elf)+"\n"+str(max_calories))