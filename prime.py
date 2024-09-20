num=int(input("enter the number:"))
for i in range(num,2):
    if num%2==0:
        print("it is not a prime number")
        break
else:
    print("it is a prime number")