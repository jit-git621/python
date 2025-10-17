# try:
#     a=1.09678
#     b=0
#     print(a/b)
# except TypeError:
#     print("somewhere type error occur")
# except Exception as e:
#     print(e)
# else:
#     print("no error occur")
# finally:
#     print("all")


# while True:
#     try :
#         a=int(input("first no=="))
#         b=int(input("second no=="))
#         print(a/b)
#         break 
#     except Exception as e:
#         print(e)

try:
    def fun(p,c):
        for i in range(p):
            for j in range(c):
                if i==0 or i==p-1 or j==0 or j==c-1 or i==j or (i==1 and j==3) or (i==3 and j==1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
except:
    print("everythimg is fine")
fun(5,5)







