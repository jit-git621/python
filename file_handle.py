# data="hello world chetan"
# count=0
# def lenth(data):
#     for i in data:
#         if " " in i:
#             global count
#             count+=1
#     return len(data)-count
# print(lenth(data))

#file handling
# f= open("dead.txt",'r')
# # f.write("i am dead")
# for i in f:
#     print(i)                               
# f.close()
# import os
# os.remove("dead.txt")
# with open ("dead.txt",'w') as f:
#     f.write("i am dead")
# with open("dead.txt",'a') as f:
#     a=f.write("\n i am alive now")
# with open("dead.txt",'r') as f:
#     print(f.read())
# with open("dead.txt",'a') as f:
#     f.write('''\n dsgdegvsedgdsvvergfd''')

# '''sick and tal'''


# f=open("dead.txt",'r')
# f.seek(10)
# print(f.tell()
# a = f.read(8)
# print(a)
# f.close()
# a=[1,2,3,4,3,4]
# b=3
# def remo(a,b):
#     c=[]
#     count=0
#     for i in range(len(a)):
#         if a[i]!=b:
#             c.insert(count,a[i])
#             count+=1
#         else:
#             c.append("_")
#     return c
            
# print(remo(a,b))


data = "ssdcodeleet"
target = "dc"
def find(data,target):
    for i in range (len(data)):
        if target in data:
            return data.index(target)
            
        else:
            return -1
print(find(data,target))