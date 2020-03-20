x="abc"
print(x.upper())
print(x)


x=10
y=20
c=x+y
print(c)
y=500
c=x+y
print(c)
#################################x
x=100

#x=datatype(input("statement"))
import keyword
print(keyword.kwlist)


x=10
y=20
com=complex(x,y)
print(isinstance(com, complex))
print(com)

############################
x=[1,2,3,4,5]
print(type(x))
#####operation over list######
m=[1,2,3,4,5,6,7]
#adding elemt at last
#1) append: 
m.append(8)
print(m)
m.append(144)
print(m)
############################
#extend
m.extend(123)
print(m)

m.extend("abc")
print(m)

d=[1,2,3,4,5,6]
a="abc"
for i in a:
    d.append(i)
    
print(d)

m.extend([1,2,34])
print(m)    

x=[1,2,3,4]
for i in x:
    print(i)
    
x=[1,2,3,4,5]
x.append([5,6,8])
print(x)

#############################
x=[[1,2,3],56,12,45,[8956,5623,7],235]
#     0     1  2  3    4           5
a=[]
for i in x:
    if(type(i)==list):
        a.extend(i)
    else:
        a.append(i)
        
print(a)
######################################
#del e
x=[1,2,3,4,5,7]
x.pop()
print(x)
###############
#insert(index,value)
x.insert(0,420)
print(x)
#################
#pop(index)
x.pop(0)
print(x)
#########
# index(value)
ind=x.index(4)
print(ind)
##########
x=[1,2,1,21,1,1,1,2,3,6,4,5]
f=x.count(1)
print(f)
###########################
x=["abc@gmail.com","rt@yahoo.com"]
x.remove("rt@yahoo.com")
print(x)
##########################################
from PIL import Image
le=["abc@gmail.com"]
ps=["abc123"]
while(True):
    print("----@@@@ WELCOME TO SHOPPING ARENA @@@---")
    print("1: login, 2: exit")
    ch=int(input("enter choice"))
    if(ch==1):
        e=str(input("enter email"))
        if(e in le):
            ind=le.index(e)
            psw=str(input("Enter password"))
            if(psw==ps[ind]):
                print("LOGIN DONE")
                print(" @@@@ LETS SHOP @@@@@@")
                while(True):
                    pro=["shoe","jacket"]
                    proimg=["C:/Users/fluXcapacit0r/Desktop/1233.jpg","‪‪E:/abcd.jpg"]
                    proprc=[999,4999]
                    print("1: view 2: price 3: order 4:exit")
                    c=int(input("Enter choice to shop"))
                    if(c==1):
                        p=str(input("Enter product name to search"))
                        if( p in pro):
                            ind=pro.index(p)
                            from PIL import Image
                            ar=Image.open(proimg[ind])
                            ar.show()
                        else:
                            print("Product out of stock")
                    elif(c==2):
                        p=str(input("Enter product name to search"))
                        if( p in pro):
                             ind=pro.index(p)
                             print("Actual cost is :",proprc[ind])
                             print("Amount to be paid :",proprc[ind])
                        else:
                            print("Product out of stock")
                    elif(c==3):
                        p=str(input("Enter product name to search"))
                        if( p in pro):
                             ind=pro.index(p)
                             print("------------------------------------")
                             print("@@@@@@@@@@@ BILL OF PRODUCT @@@@@@@@@@@@")
                             print("Product is :",p)
                             print("Amount to be paid :",proprc[ind])
                             print("-------------------*************------------------")
                        else:
                            print("product out of stock")
                    elif(c==4):
                        break
            else:
                print("invalid password")
        else:
            print("Invalid Email")
    elif(ch==2):
        break 
    else:
        print("Invalid choice")
##################################################################

a=[]
print(type(a))        
        
        
        
a={}
print(type(a))

a={1,2,3}
print(type(a))        
###########################
data={"name":"abc","class":5}
print(type(data)) 
# key are unique
a={1:1,2:2,1:5,3:7}
print(a)
########################
data={"abc":339,"t":235}
#data[key]=value
data["raju"]=340
print(data)        
        
data.update({"tina":235,
             "rajeev":320,
             "raghu":200})
print(data)
        
        
#del elemt 
data.pop("tina")
print(data)
############################3
data.clear() 
print(data)