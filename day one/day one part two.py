
max_calories=[1,2,3]
txt_input = open("input.txt","r")

tbl_input=txt_input.read().split("\n\n")
print(tbl_input)
for i in range(0,len(tbl_input)):
    calories = sum(map(int,tbl_input[i].split("\n")))
    if calories>max_calories[0] :
        max_calories[0]=calories
        max_calories.sort()


print(str(sum(max_calories)))