#numpy library python : base for machine learning
import numpy as np
d=[300,400,200,300]
t=[4,3,6,7]
s=d/t
print(s)
##############################
#creating array from list
dis=np.array([300,400,200,300])
tim=np.array([4,3,6,7])
sp=dis/tim
print(sp)
#################################
#creating array from tuple
#################################
t=(1,2,3,45)
print(type(t))
t=("a",)
print(type(t))
################################
tuple_arr=np.array((23,454,78,4,56))
print(tuple_arr)
print(type(tuple_arr))
###############################
t=(1,2,3,45)
tuple_arr=np.array(t)
print(tuple_arr)
print(type(tuple_arr))

###############################
l=[[1,2,3],[45,56,89],[7,8,9],[45,5,6]]
arr=np.array(l)
print(arr)
######################################
#####print dimension of array#####
print(arr.ndim)
######shape
print(arr.shape)
######size###number of element
print(arr.size)
##########
print(arr.dtype)
###################################
l=[[1,2,3],[45,56,89],[7,8,9],[45,5,6]]
arr=np.array(l,dtype="float")
print(arr)
print(arr.dtype)
#####################################
import random
print(random.random())
#####################################
ar=np.random.random((2,2))
print(ar)
#####################################
a=np.zeros((4,6))
print(a)
#give zero ndarray which has 4 row and 6 col
#####################################
s=[]
for i in range(0,21,+5):
    s.append(i)
print(s)
arr=np.array(s)
print(arr)
########################################
t=np.arange(0,21,5)
print(t)
#######################
t=np.arange(20,0,-5)
print(t)
########################################
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
arr=np.array(a)
print(arr)
#########################################
d=arr.reshape(2,2,3)
print(d)
######################################
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
arr=np.array(a)
f=arr.flatten()
print(f)
##########################################
###slicing###########################
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
arr=np.array(a)
print(arr)
print(arr[0:,0:2])
print(arr[0:,::-1])

###################################
l=[1,2,3,4,5,6]
print(l[0:])
print(l[0::+2])
print(l[len(l)-1::-1])
print(l[::-1])

################################3
#basic operation
l=[1,2,3,4,5,6]
arr=np.array(l)
d=arr*5
print(d)
div=arr/2
print(div)
#####################
l=[1,2,3,4,5,6]
arr=np.array(l)
d=arr**5
d
###################################
l=[1,2,3,4,5,6]
a=list(map(lambda x:x**2,l))
print(a)
###############################
###Transpose method 
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
arr=np.array(a)
arr_t=arr.T
print(arr)
print(arr_t)

#####################################
#unary operation
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
arr=np.array(a)
print(arr.max())
print(arr.min())
### row axis =1 amd col axis= 0
a=[[1,2,3,4],[5,6,7,8],[9,1,0,122]]
arr=np.array(a)
print(arr.max(axis=1))
print(arr.max(axis=0))
#####################################
print(arr.min(axis=1))
print(arr.min(axis=0))
##############################
print(arr.sum())
print(arr.sum(axis=1))
print(arr.sum(axis=0))
####################################
## binary operarion on array
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[23,4,5],[8,89,5]])
print(a+b)
#######################################################
#universal opeartion##########

a=25
import math
d=math.sqrt(a)
print(d)

import numpy as np
a=np.array([25,225,169,196])
sqrt_array=np.sqrt(a)
print(sqrt_array)
#####################
d=[]
a=[25,225,169,196]
for i in a:
    d.append(math.sqrt(i))
arr=np.array(d)
print(arr)
###############################
#sorting#######
a=[[1,2,3,4],[5,6,7,8],[9,1,0,122]]
arr=np.array(a)
print(np.sort(arr))
print(np.sort(arr,axis=1))
print(np.sort(arr,axis=0))
###############################
###stacking##########
a=np.array([[1,2,3],
            [4,5,6]])
b=np.array([[23,4,5],
            [8,89,5]])
arr_h=np.hstack((a,b))
print(arr_h)
print(arr_h.shape)
arr_v=np.vstack((a,b))
print(arr_v)
print(arr_v.shape)
###################################
###################################
#broadcasting#######
#row==col

a=np.array([[1,2,3],
            [4,5,6]])
b=np.array([[23,4,5],
            [8,89,5]])
d=a*b
print(d)
###error##
#ValueError: operands could not be broadcast together with shapes (2,2) (2,3) 
a=np.array([[1,2],
            [4,5]])
b=np.array([[23,4,5],
            [8,89,5]])
d=a*b
print(d)
#######################################
import numpy as np
a=np.array([[1,2,3],
            [56,2,12],
            [56,2,10]])
print(a.sum(axis=1))
print(a.sum(axis=0))
print(a.trace())# sum of diagnal
###################################
#datatype:
a={}
print(type(a))
a={"name":"raja","class":5,
   "name":"kumar"}
print(a)
data={}
#student add
#data[key]=value
data["suraj"]=70
print(data)
# adding multiple
data.update({"raj":99,
             "sameer":86,
             "ramesh":36})
print(data)
print(data["sameer"])
print(data[86])

#modify 
data.update({"raj":100})
print(data)
###############################
#del key and value using pop(key)
data.pop("raj")
print(data)
#######################
#extract all keys
print(data.keys())
print(data.values())
######################
data.clear()
print(data)
####################################
####
data={}
while(True):
    print(" LOGIN LAYER ")
    print("1: Register 2: login ")
    ch=int(input("Enter choice>>: "))
    if(ch==1):
        e=str(input("Enter Email Address :"))
        if(e in list(data.keys())):
            print("Email is used by some on else ")
        else:
            pas=str(input("Create password :"))
            data[e.lower()]=pas
            print("Created sucessfully ")
    elif(ch==2):
        e=str(input("Enter Email Address :"))
        if ( e.lower() in list(data.keys())):
             psw=str(input("Enter password >> :"))
             p=data[e.lower()]
             if(p==psw):
                 print("Aceess granted : ")
             else:
                 print("Wrong password")
        else:
            print("Invalid ID")
    elif(ch==3):
        break
                 


