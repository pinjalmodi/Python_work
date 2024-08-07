class Bank:
    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello",cname,"Your Account Number",acno,"has balance of",balance,"Rs")
    def deposite(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient Balance")

    def checkBalance(self):
        print("Current Balance:",self.balance)


b1=Bank()
b1.openAccount(101,"Jigar",1000)

while True:
    print("*"*40)
    print("1. Deposite")
    print("2. Withdraw")
    print("3. Balacne")
    print("4.Exit")

    choice=int(input("Enter your choice"))
    if choice==1:
        amount=(int(input("Enter amount to deposite")))
        b1.deposite(amount)
        print("*"*40)
    elif choice==2:
        amount=(int(input("Enter amount to Withdraw")))
        b1.withdraw(amount)
        print("*"*40)
    elif choice==3:
        b1.checkBalance()
        print("*"*40)
    elif choice==4:
        print("Thank you for using our services")
        print("*"*40)
        break

    else:
        print("Invalid entry..Please try again later")
        print("*"*40)

        
    
