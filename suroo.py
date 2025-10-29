'''create a inventery management system
production
quality
price
amount
revenue


sell
buy
update
display product list'''
import random

class ims:
    def __init__(self):
        self.product_name=[]
        self.quantity=[]
        self.price=[]
        self.amount=[]
        self.data3=[]
    def buy(self,p_name,p_quantity,p_price):
        self.product_name.append(p_name)
        self.quantity.append(p_quantity)
        self.price.append(p_price)
        self.amount.append(p_quantity*p_price)
        
        self.data2=dict(zip(["price","quantity"],[p_price,p_quantity]))
        self.data3.append(self.data2)
        self.data=dict(zip(self.product_name,self.data3))
        
    def display(self):
        print(dict(self.data))

    # def sale(self):
    #     p_name1=input("enetr product name")
    #     qty =int(input(f"enter the quantity of {p_name1}"))
    #     if p_name1 in self.data:
    #         self.data.update(self.product_name,self.quantity[0]-qty)





creature=ims()
while True:
    product=input("enter product name:-")
    quantity=int(input("enter quantity of product:-"))
    price=int(input("enter the price"))
    creature.buy (product,quantity,price)
    choice=input('''press Y to enter more itam
                 press N to exit:-  ''')
    if choice !='y' or choice!='Y':
        break
creature.display()
# creature.sale()


