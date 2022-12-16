txt_input=open("day 6\input.txt","r")
datastream=txt_input.readline()
last4char=[]
i=0
markerfound=False
while(not markerfound and i<len(datastream)):
    if(len(last4char)<4):
        last4char.append(datastream[i])
    elif last4char.__contains__(datastream[i]) :
        del last4char[0]
        last4char.append(datastream[i])
    elif (last4char[0]!=last4char[1] and last4char[0]!=last4char[2] and last4char[0]!=last4char[3] and last4char[1]!=last4char[2] and last4char[1]!=last4char[3] and last4char[2]!=last4char[3] ) :
        del last4char[0]
        last4char.append(datastream[i])
        markerfound=True
    else :
        del last4char[0]
        last4char.append(datastream[i])

    i+=1
print(last4char)
print(i-1)