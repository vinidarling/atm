num= int(input("enter the number:"))
sum=0
l=len(str(num))
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**l
    temp=temp//10
if sum==num:
    print("it is a amstrong")
else:
    print(" not an armstrong")