########## 2nd batch (Evening) ##########
        
################################
x=100
x=int(input("enter number :"))
##########################
x=523.23
print(type(x))
################################
r=int(input("enter number :"))
i=float(input("Enter number :"))
com=complex(r,i)
print(com)
print(type(com))
######################################
data=[1,2,3,4]#homo array
print(type(data))                

a=[1,2,3,4,5,6,7]
#indexing
print("my value is :",a[3] )
#234
print(a[1:3])
print(a[1:4]) 
#[3,4,5,6]
print(a[2:6])
####[1,3,5,7]
print(a[0:])
print(a[0::+2])
print(a[::-1])
##############list operation############
l=[1,2,3,4,5,6,7]
#adding element at last
#data.append(value)
l.append(8)
print(l)
#[1, 2, 3, 4, 5, 6, 7, 8] chage will be according to new data
print(len(l))

####################################
#index 
l=[23,56,45,223,568,56212,7895]
ind=l.index(223)
print(ind)
#######################
#data.insert(index,value)
l.insert(3,50000)
print(l)
##########################
l=[23,23,1,2,12,56,5,6,89,56,56,56,23,45,7]
f=l.count(56)
print(f)
###########################
###deleting element###
data=["a","b","c","d","e","f"]
#element del form last data.pop()
data.pop()
print(data)
#elemt del from speific index 1) pop(index) , del index
data.pop(0)
print(data)
### del 
del data[0]
print(data)
#####
a=["a","b","a","c"]
a.remove("a")
print(a)
#############
a.clear()
print(a)
###########################
#data.extend(value) comment value: iterable
l=[1,2,3,4]

l.append(2)
print(l)

l.extend(2)#error
print(l)

#extend(string , list)
l.extend("abc")
print(l)
###backend
a=[1,2,3]
d="abc"
for i in d:
    a.append(i)
    print(a)

a.append("tryeu")
print(a)

a.extend([1,2,3,4])
print(a)
###################################
a=[231,12,1,4586,223,5658,412,15565,15]
a.sort()
print(a)
###################
a.reverse()
print(a)
###################################
#####Student management system#####
#database
li=[]
ln=[]
lb=[]
lf=[]
while(True):
    print("------------------------------------")
    print("@@@@@@@@@@ WELCOME TO MITRC SCHOOL @@@@@@@@@@@@")
    print(" ")
    print("1: Add Student Detail ")
    print("2: Del student Detail ")
    print("3: Modify student Detail ")
    print("4: Show Detil")
    print("5: Exit")
    ch=int(input("Enter Choice As Mention Above"))
    if(ch==1):
        i=str(input("Generate Id"))
        n=str(input("Enter Full Name"))
        b=str(input("Enter Branch"))
        f=float(input("Enter Fee "))
        li.append(i)
        ln.append(n)
        lb.append(b)
        lf.append(f)
        print(" Student Detail Added Sucessfully ")
    elif(ch==2):
        i=str(input("Enter Id of student"))
        if( i in li):
            ind=li.index(i)
            li.pop(ind)
            ln.pop(ind)
            lb.pop(ind)
            lf.pop(ind)
            print(" Student Data Del Sucessfully ")
        else:
            print("ID NOT IN DATABASE")
    elif(ch==3):
        i=str(input("Enter Id of student"))
        if( i in li):
            ind=li.index(i)
            nn=str(input("Enter modify name "))
            ln[ind]=nn
            nb=str(input("Enter New Branch "))
            lb[ind]=nb
            nf=float(input("Enter Modify Fees"))
            lf[ind]=nf
            print(" Data Modify Sucessfully ")
        else:
            print("Id not in database")
    elif(ch==4):
        i=str(input("Enter Id of student"))
        if( i in li):
            ind=li.index(i)
            print("-------------Student Detail ----------------")
            print(" ")
            print("Id is: ", li[ind])
            print("Name of student is :",ln[ind])
            print("Branch is :",lb[ind])
            print("Fees is :",lf[ind])
            print(" ")
            print("-----------------************----------------")
        else:
            print("ID not in database")
    elif(ch==5):
        break
    else:
        print("INVALID CHOICE")
            
            
#######################################################################
            
                
            
        
l=[1,2,3,4,5,6,"adf",8]
l[6]=7
print(l)