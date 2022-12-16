text_input= open("day three\input.txt","r")
prioSum=0
rucksacks=text_input.readlines()
nbgroups=int(len(rucksacks)/3)
groups=[]
i=0
j=0
#séparation en groupe de 3
for line in rucksacks:
    if i%3==0:
        groups.append(line)
        j=int(i/3)
    else:
        groups[j]+=line
    i+=1
for group in groups:
    S1,S2,S3=group.split("\n")[0],group.split("\n")[1],group.split("\n")[2]
    for j in range(0,len(S1)):
        if S1[j] in S2 and S1[j] in S3:
            #ord renvoie un nb pour chaque char unicode
            #cependant, les miniscule commence a 97, et les majuscule a 65
            #on sépare donc Maj et Min
            if (S1[j].isupper()):
                prioSum+=ord(S1[j])-38
                
                print(S1[j]+" "+str(ord(S1[j])-38))
                break
            else :
                prioSum+=ord(S1[j])-96#la prio des Majs commence a 27
                print(S1[j]+" "+str(ord(S1[j])-96))
                break
print(prioSum)