a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if c<a>b:
    print("a is greater")
elif c<b>a:
    print("b is greater")
elif a<c>b:
    print("c is greater")
else:
    print("all are equal")
