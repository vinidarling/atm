y=int(input("enter the cash:"))
if v<=9999:
    print("donot go to shop")
elif v>=10000 and v<20000:
    print("redmi")
elif v>=20000 and v<30000:
    print("oppo")
elif v>=30000 and v<50000:
    print("oneplus")
elif v>=50000 and v<100000:
    print("sumsung")
else:
    print("back to home")