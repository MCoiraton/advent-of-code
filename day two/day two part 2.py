txt_input = open("day two\input.txt","r")
guide=txt_input.read().split("\n")
final_r=0

def result (j1,j2):
    r=0
    match(j1):
        case "A":
            match(j2):         
                case "X":
                    r+=3
                case "Y":
                    r+=4 
                case "Z" :
                    r+=8
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
                    r+=2
                case "Y":
                    r+=6 
                case "Z" :
                    r+=7
    return(r)

def read(i):
    match(i):
        case "A":
            return 1
        case "B":
            return 2
        case "C":
            return 3
        case "X":
            return 0
        case "Y": 
            return 3
        case "Z":
            return 6

for i in range(0, len(guide)):
    final_r+=result(guide[i].split(" ")[0],guide[i].split(" ")[1])

print(final_r)