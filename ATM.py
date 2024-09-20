print("Welcome to Indian Overseas Bank ATM")
print("Insert your card")
b1=50000
a=7777
print("Enter your pin")
pin=int(input("a:"))
if pin==a:
    print("select the language")
    print("1.English")
    print("2.Hindi")
    print("3.Telugu")
    n=int(input("n:"))
    if n==1:
        print("language followed by English")
    elif n==2:
        print("language followed by Hindi ")
    elif n==3:
        print("language followed by Telugu")
    else:
        print("select the required language")
    print("1.with drawl")
    print("2.Balance enquiry")
    print("3.pin Generation")
    print("4.pin change")
    print("5.Deposit")
    print("6.exit")
    n=int(input("n:"))
    if n==1:
        print("1.savings account")
        print("2.current account")
        n = int(input("n:"))
        if n == 1:
            print("through savings")
        elif n == 2:
            print("through current")
        amount = int(input("Enter the amount required:"))
        print("the transaction is under process please wait")
        if amount>50000:
            print("insufficient balance")
        else:
            print("collect your cash")
        print("1.check balance")
        print("2.exit")
        n=int(input("n:"))
        if n==1 and amount<=50000:
                a1=b1-amount
                print("the balance is",a1)
        else:
            print("the balance is",b1)
        if n==2:
            print("exit")
        print("collect the receipt")
    elif n==2:
        print("balance is",b1)
        print("collect the receipt")
    elif n==3:
       # print("go through the otp")
        number1=int(input("enter the mobile number:"))
        number2=int(input("enter the otp number:"))
        print("please enter a pin as required")
        n=int(input("n:"))
        print("re enter the pin")
        m=int(input("m:"))
        if n==m:
            print("pin generated successfully")
        else:
            print("check the pin u have entered")
    elif n==4:
        #print("go through the acc.no and mob.no")
        n1=int(input("enter the acc.no:"))
        n2=int(input("enter the mob.no:"))
        n3=int(input("enter the otp.no:"))
        n4=int(input("enter the old.pin:"))
        n5=int(input("enter the required new.pin:"))
        n6=int(input("re enter the new.pin:"))
        if n5==n6:
            print("pin changed successfully")
        else:
            print("check the pin u have entered")
    elif n==5:
        n1=int(input("enter the mob.no:"))
        n2=int(input("enter the acc.no"))
        Deposit=int(input('enter the amount for Deposit:'))
        print("keep the cash in it")
        print("transaction is under process...wait for a while")
        print("your amount deposited successfully")
        print("1.check balance")
        print("2.exit")
        n=int(input("n:"))
        if n==1:
            v1=b1+Deposit
            print("the balance is",v1)
        elif n==2:
            print("exit")
        else:
            print("select the valid key")
    elif n==6:
        print("exit")
else:
    print("invalid pin")
print("please collect u r card")
print("THANK YOU .VISIT AGAIN")


