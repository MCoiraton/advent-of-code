txt_input = open("input.txt","r")
guide=txt_input.read().split("\n")
final_r=0

def result (j1,j2):
    r=0
    match(j1):
        case "A":
            match(j2):         
                case "X":
                    r+=4
                case "Y":
                    r+=8 
                case "Z" :
                    r+=3
        case "B":
            match(j2):
                case "X":
                    r+=1
                case "Y":
                    r+=5
                case "Z" :
                    r+=9
        case "C":
            match(j2):
                case "X":
                    r+=7
                case "Y":
                    r+=2
                case "Z" :
                    r+=6
    return(r)

for i in range(0, len(guide)):
    final_r+=result(guide[i].split(" ")[0],guide[i].split(" ")[1])

print(final_r)