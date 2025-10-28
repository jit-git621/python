import random 
class atm :
    def __init__(self):
        self.account_no=random.randrange(1000000000,9999999999)
        print(f"account no={self.account_no}")
        self.balance = 1000
    def withdrow(self,amount):
        if amount<=self.balance:
            print(f"amount withdrw by you is ={amount}")
            self.balance-=amount
        else:
            print("insufficiant balance ")
    def deposite(self,amount):
        self.balance+=amount
        print(f"succesfully added{amount}")
    def check_balance(self):
        new=int(input("enter account no="))
        if new==self.account_no:
            print(f"your balance is {self.balance}")

    
chetan=atm()
chetan.check_balance()

