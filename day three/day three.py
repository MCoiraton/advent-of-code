rucksacks= open("day three\input.txt","r")
prioSum=0
for line in rucksacks.readlines():
    #séparation des deux compartiments
    C1, C2 = line[0:int(len(line)/2)], line[int(len(line)/2):]
    #on regarde quelle lettre se trouve en double
    for j in range(0,len(C1)):
        if C1[j] in C2:
            #ord renvoie un nb pour chaque char unicode
            #cependant, les miniscule commence a 97, et les majuscule a 65
            #on sépare donc Maj et Min
            if (C1[j].isupper()):
                prioSum+=ord(C1[j])-38
                
                print(C1[j]+" "+str(ord(C1[j])-38))
                break
            else :
                prioSum+=ord(C1[j])-96#la prio des Majs commence a 27
                print(C1[j]+" "+str(ord(C1[j])-96))
                break

print(prioSum)
