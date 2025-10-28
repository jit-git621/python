data='abcxfghpqrssd'
new=[]
a=''
a=a+data[0]
for i in range(1,len(data)):
    if ord(data[i])-1==ord(data[i-1]):
        a+=data[i]
    else:
        new.append(a)
        a=data[i]
new.append(a)
print(new)  