def scalingE1(myLower,myUpper,ans):
    f=False
    while myLower < 0.5 and myUpper < 0.5:
        ans+="0"
        myLower *= 2
        myUpper *= 2
    if myLower > 0.5 and myUpper > 0.5:
        f=True
        x = scalingE2(myLower,myUpper,ans)
    if f:
        return x
    else:
        return [myLower, myUpper,ans]



def scalingE2(myLower,myUpper,ans):
    f = False
    while myLower > 0.5 and myUpper > 0.5:
        ans+="1"
        myLower = (myLower - 0.5) * 2
        myUpper = (myUpper - 0.5) * 2
    if myLower < 0.5 and myUpper < 0.5:
        f = True
        x=scalingE1(myLower, myUpper,ans)
    if f:
        return x
    else:
        return [myLower, myUpper,ans]


file=open("InputForCompress.txt", "r").read()
output=open("OutPutCompress.txt", "w")
ans=""
chars=[]
p=[]
lower=[]
upper=[]
myLower=0
myUpper=1
k=1

for character in file:
    if(chars.count(character)):
        continue
    else:
        chars.append(character)
    p.append(file.count(character) / len(file))
lower.append(0)
upper.append(p[0])
for i in range(len(p)-1):
    lower.append(upper[i])
    upper.append(lower[i+1]+p[i+1])
index=chars.index(file[0])
myLower=lower[index]
myUpper=upper[index]
x=scalingE1(myLower, myUpper,ans)
myLower=x[0]
myUpper=x[1]
ans=x[2]
smallestRange=min(p)

while True:
    if(1/pow(2, k)) < smallestRange:
        break
    k=k+1

for i in range(len(file)-1):
    myrange = myUpper-myLower
    index = chars.index(file[i+1])
    myUpper = myLower + myrange * upper[index]
    myLower = myLower + myrange * lower[index]
    x = scalingE1(myLower, myUpper,ans)
    myLower = x[0]
    myUpper = x[1]
    ans=x[2]

ans+="1"
for x in range(k-1):
    ans+="0"


output.write(ans)
output.close()