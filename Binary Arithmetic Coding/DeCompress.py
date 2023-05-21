def binaryTodecimal(n):
    decimal = 0
    power = 1
    while n > 0:
        rem = n % 10
        n = n // 10
        decimal += rem * power
        power = power * 2

    return decimal

def scalingE1(myLower,myUpper,code):
    f=False
    while myLower < 0.5 and myUpper < 0.5:
        code=code[1:]
        myLower *= 2
        myUpper *= 2
    if myLower > 0.5 and myUpper > 0.5:
        f=True
        x = scalingE2(myLower,myUpper,code)
    if f:
        return x
    else:
        return [myLower, myUpper,code]


def scalingE2(myLower,myUpper,code):
    f = False
    while myLower > 0.5 and myUpper > 0.5:
        code=code[1:]
        myLower = (myLower - .5) * 2
        myUpper = (myUpper - .5) * 2
    if myLower < 0.5 and myUpper < 0.5:
        f = True
        x=scalingE1(myLower, myUpper,code)
    if f:
        return x
    else:
        return [myLower, myUpper,code]


file = open("InputForDecompress.txt", "r")
output = open("outputdecompress.txt", "w")
x=file.readline()
y=file.readline()
chars=[ str(v) for v in x.split(",")]
p = [ float(l) for l in y.split(",")]
comp_code=file.readline()

code=""
ans=""
k=1
lower=[]
upper=[]
myLower=0
myUpper=1
min_prob=min(p)

while(1/(pow(2,k)) > min_prob):
    k+=1

code=(comp_code[0:k])
bin=binaryTodecimal(int(code))/pow(2,k)

lower.append(0)
upper.append(p[0])
for i in range(len(p)-1):
    lower.append(upper[i])
    upper.append(lower[i+1]+p[i+1])
while(len(comp_code)>k):
  for i in range(len(p)):
     if lower[i]< bin < upper[i]:
        ans+=chars[i]
        myrange = myUpper - myLower
        myUpper = myLower + myrange * upper[i]
        myLower = myLower + myrange * lower[i]
        x = scalingE1(myLower, myUpper, comp_code)
        myLower = x[0]
        myUpper = x[1]
        comp_code = x[2]
        code = (comp_code[0:k])
        bin = binaryTodecimal(int(code)) / pow(2, k)
        bin = (bin - myLower) / (myUpper - myLower)


bin = binaryTodecimal(int(code)) / pow(2, k)
bin = (bin - myLower) / (myUpper - myLower)
for i in range(len(p)):
    if lower[i] < bin < upper[i]:
        ans += chars[i]


output.write(ans)
file.close()
output.close()