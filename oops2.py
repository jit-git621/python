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


# # count1=0
# def count(fct):
#     count1=0

#     def wrapper(n):
#         nonlocal count1
#         count1+=1
#         re=fct(n)
#         print(re)
#     return wrapper()
# @count
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
