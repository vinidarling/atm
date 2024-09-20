num=int(input("num:"))
temp1=num
temp2=num
count=0
while num>0:
    count=count+1
    num=num//10
sum=0
while temp1>0:
    b=temp1%10
    sum=sum+b**count
    temp1=temp1//10
if sum==temp2:
    print("armstrong")
else:
    print("not a armstrong")