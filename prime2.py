num=int(input("enter the number:"))
for i in range(0,num):
    if num%2==0:
        print(" not prime number")
        break
else:
    print("prime")