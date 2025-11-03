'''encapsulation => it is a concept to hide your data by make them private we use access modifier (_) for making our data privete '''
''''''
# class c1:
#     __age=90
#     def __init__(self):
#         print("i am c1 constructor")
#     def __display(self):  # this access private variable
#         print(c1.__age)
#     def call_display(self):
#         return c1.__display(self)
# obj=c1()
# # print(obj.__age)  # not access to private variable
# # obj.display()  # in this method access private variable 
# print(obj._c1__age)  # this is second method but not recommended
# obj.call_display()  # private method ko call karega or access ho jayega  
'''partially encapsulation(protected encapsulation its only devloper ke liye hai) and fully encapsulation'''
# class c1:
#     _data=90
#     _data=8
#     def m1(self,a,b):
#         self.a=avfrvfrvfr4vfr4vrf
#         self.b=b
#     def display(self):
#         print(self.a,self.b)
# obj=c1()
# print(obj._data)

# class bank:
#     def __init__(self):
#         self.__accountNo=int(input("Enter a account number : "))
#         self.__balance=int(input("Enter a current account balance : "))
#     def display(self):
#         print(f"you account number is {self.__accountNo}")
#         print(f"you current account balance is {self.__balance}")
# obj=bank()
# obj.display()
# print(obj._accountNo)
# obj1=bank()
# obj.display()