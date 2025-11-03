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
        
        self.data2=dict(zip(["quantity","price"],[p_quantity,p_price]))
        self.data3.append(self.data2)
        self.data=dict(zip(self.product_name,self.data3))

        
    def display(self):
        print(dict(self.data))
        # price(self.data.get(self.product_name))

    def sale(self):
        p_name1=input("enetr product name")
        qty =int(input(f"enter the quantity of {p_name1}"))
        b=self.data.get(p_name1)
        if p_name1 in self.data:
            self.data.update({p_name1:self.quantity-qty})


creature=ims()
while True:
    product=input("enter product name:-")
    quantity=int(input("enter quantity of product:-"))
    price=int(input("enter the price"))
    creature.buy (product,quantity,price)
    choice=input('''press Y to enter more itam
                 press N to exit:-  ''')
    if choice =='N' or choice=='n':
        break
creature.display()
creature.sale()



