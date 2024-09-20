# s1=input("enter the str:")
# s2=input("enter the str:")
# ascii=[0]*91
# flag=True
# for i in s1:
#     if i>='a' and i<='z':
#         ele=ord(i)-32
#         ascii[ele]+=1
#     elif i>='A' and i<='Z':
#         ascii[ord(i)]+=1
# for i in s2:
#     if i>='a' and i<='z':
#         ele=ord(i)-32
#         ascii[ele]-=1
#     elif i>='A' and i<='Z':
#         ascii[ord(i)]-=1
# for i in range(65,91):
#     if ascii[i]!=0:
#         flag=False
#         break
# if flag==True:
#     print("annagram")
# else:
#     print("not a annagram")
a=input("a:")
b=input("b:")
ascii=[0]*91
flag=True
for i in a:
    if i>='a' and i<='z':
        ele=ord(i)-32
        ascii[ele]+=1
    elif i>='A' and i<='Z':
        ascii[ord(i)]+=1
for i in b:
    if i>='a' and i<='z':
        ele=ord(i)-32
        ascii[ele]-=1
    elif i>='A' and i<='Z':
        ascii[ord(i)]-=1
for i in range(65,91):
    if ascii[i]!=0:
        flag=False
        break
if flag==True:
    print("anagram")
else:
    print("not a anagram")
# d={'name':'vini','age':21,'ffood':'biryani','dob':2002}
# key=0
# for i,j in d.items():
#     if j ==21:
#         key=i
#         break
# if key!=0:
#     del d[key]
# print(d)
# def pairs(a,t,n):
#     p=[]
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if a[j]-a[i]==t:
#                 p.append((a[i],a[j]))
#
#     return p
# a=[1,2,3,4]
# t=2
# n=len(a)
# s=pairs(a,t,n)
# print("the count is",s)
# sen=input()
# ns=''
# w=""
# for i in sen:
#     if ord(i)!=32:
#         w=w+i
#         ns=w+ns
#         w=''
a=input("a:")
b=input("b:")
ascii=[0]*91
flag=True
for i in a:
    if i>='a' and i<='z':
        ele=ord(i)-32
        ascii[ele]+=1
    elif i>='A' and i<='Z':
        ascii[ord(i)]+=1
for i in b:
    if i>='a' and i<='z':
        ele=ord(i)-32
        ascii[ele]-=1
    elif i>='A' and i<='Z':
        ascii[ord(i)]-=1
for i in range(65,91):
    if ascii[i]!=0:
        flag=False
        break
if flag:
    print("annagram")
else:
    print("np")
