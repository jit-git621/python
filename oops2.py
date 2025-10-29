# def mydeco(function_name):
#     def  wrapper():
#         c=function_name(10,5)
#         print(c*10)
#     return wrapper()
# @mydeco
# def sub(a,b):
#     c=a-b
#     return c

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         result = func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#         return result
#     return wrapper

# @my_decorator
# def say_hello(name):
#     print(f"Hello, {name}!")

# say_hello("Alice")


# class MyClass:
#     data=30
#     def __init__(self):
#         print("MyClass object created.")

#     def __del__(self):
#         print("MyClass object destroyed.")

# # Create an object
# obj = MyClass()
# obj.data
# # Delete the object (or let its reference count drop to zero)
# print(obj.data)



# class c11:
#     data=99999999
#     def m1 (self):
#         self.data
       
# bj=c11()
# bj.m1()
# print(bj.data)
# class c3:
#     def __init__(self):
#         print("a anm")
#     def __del__(self):
#         print("no above")

# c1=c3()


# def name(fct):
#     global count
#     count=0
#     def inner2(n):
#         global count
#         count+=1
#         return fct(n)
#     return inner2
# @name
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)

# print(fact(5))
# print(fact(3))
# print(count)


# m=["name","namo","narrow"]
# def pref(m):
#     nu=m[0]
#     for i in m[1:]:
#         while not i.startswith(nu):
#             nu=nu[:-1]
#             if not nu:
#                 return " "
#     return nu
# print(pref(m))


# a=[1,3,6,8,56]
# b=[3,7,9,11,25]
# i,j=0,0
# k=3
# new=[]
# while i<4 or j<4:
#     if i<max(len(a),len(b)):
#         if a[i]<=b[j]:
#             t=min(a[i],b[j])
#             new.append(t)
#             if i<len(a):
#                 i+=1
    
#         if a[i]>=b[j]:
#             new.append(b[j])
#             if j<len(b):
#                 j+=1
#     elif a==[] :
#         new.append(b[j:])
#     elif b==[]:
#         new.append(a[i:])
#     else:
#         print("complete")

# print(new)


# class c1:
#     data=106
#     def m1(self):
#         print("i am m1 from c1")
# class c2(c1):
#     name='angrad'
# b1=c2()
# print(b1.data)
# b1.m1()

# class above_18:
#     voteer_id=217652
#     def going_office(self):
#         print("writing in office")
#     def play(self):
#         print("playing s**")

# class below_18(above_18):
#     def eting(self):
#         print("eating snacks")
#     def play(self):
#         print("playing football")

# rahil=below_18()
# rahil.eting()


# class c1:
#     def __init__(self):
#         print("raju kutriya")

# class c2(c1):
#     def __init__(self):
#         print("tere pass dusra plan he ")
#         super().__init__()

# class c3(c2):
#     def __init__(self):
#         print("inko sone ka katora de to bhi bhik hi mange ge")
#         super().__init__()
# class c4(c3):
#     def __init__(self):
#         print("ghoda kaha he")
#         super().__init__()
# class c5(c4):
#     def __init__(self):
#         print("ghash kha raha he ")
#         super().__init__()
# class c6(c5):
#     def __init__(self):
#         print("ghash kaha he")
#         super().__init__()
# class c7(c6):
#     def __init__(self):
#         print("ghoda kha gaya na l***n k3")
#         super().__init__()
    

# obj=c7()






