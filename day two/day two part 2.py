txt_input = open("input.txt","r")
guide=txt_input.read().split("\n")
final_r=0

def result (j1,j2):
    r=0
    match(j1):
        case "A":
            match(j2):         
                case "X":
                    r+=0
                case "Y":
                    r+=3 
                case "Z" :
                    r+=6
            r+=1
        case "B":
            match(j2):         
                case "X":
                    r+=0
                case "Y":
                    r+=3 
                case "Z" :
                    r+=6
            r+=2
        case "C":
            match(j2):         
                case "X":
                    r+=0
                case "Y":
                    r+=3 
                case "Z" :
                    r+=6
            r+=3
    return(r)

def read(i):
    match(i):
        case "A":
            return 1
        case "B":
            return 2

for i in range(0, len(guide)):
    final_r+=result(guide[i].split(" ")[0],guide[i].split(" ")[1])

print(final_r)