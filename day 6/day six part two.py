txt_input=open("day 6\input.txt","r")
datastream=txt_input.readline()
last14char=[]
i=0
markerfound=False
while(not markerfound and i<len(datastream)):
    if(len(last14char)<14):
        last14char.append(datastream[i])
    elif(len(set(last14char)) == len(last14char)): 
        markerfound=True
    else :
        del last14char[0]
        last14char.append(datastream[i])

    i+=1
print(last14char)
print(markerfound)
print(i-1)