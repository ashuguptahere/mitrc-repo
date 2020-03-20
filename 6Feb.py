#machine Learning Library Matplotlib
#matplotlib.pyplot 
#all above are used for visualization purpose

#import lib
import matplotlib as pl
import matplotlib.pyplot as plt
## data
x=[4,3,2,5]
y=[3,1,2,5]
plt.plot(x,y,color="red")
plt.show()
#######################################
x=[1,2,3,4,5]
y=[1,2,3,4,5]
plt.plot(x,y,color="red")
plt.show()
################################
#bar plot 
a=["r","g","b"]
x=[1,2,3,4,5]
y=[1,2,3,4,5]
plt.bar(x,y,color=a)
plt.xlabel("number of sample")
plt.ylabel("frequency")
plt.title(" my plot")
plt.show()
############
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[100,200,300,400,500]
plt.bar(x,y)
plt.show()
###################
#histogram
sal=[100,200,175,145,1223,4421,112,23]
plt.hist(sal)
plt.show()
#######################################
sal=[100,200,50,70,90,110,240]
plt.hist(sal)
plt.show()
#################################
sal=[100,200,175,145,1223,4421,112,23]
plt.hist(sal,orientation="horizontal",color="red",)
plt.show()
##########################
#scatter plt
age=[23,30,45,24,36]
sal=[5000,3000,4500,5600,8922]
plt.scatter(age,sal,color="black")
plt.show()

####################
###muliple plt
x1=[1,2,4,5]
y1=[1,3,3,1]
x2=[2,3,4,5]
y2=[5,4,3,2]
plt.plot(x1,y1,color="blue")
plt.scatter(x2,y2,color="red")
plt.show()
##########################
#scatter plt
age=[23,30,45,24,36]
sal=[5000,3000,4500,5600,8922]
plt.scatter(age,sal,color="black")
plt.xlabel("age")
plt.ylabel("sal")
plt.title("age vs sal")
plt.show()

#################################
x1=[1,2,3,4]
y1=[1,2,2,1]

x2=[1,2,3,4]
y2=[3,1,1,3]
plt.scatter(x1,y1,color="red")
plt.scatter(x2,y2,color="blue")
plt.show()
#######################################
#customize plot 
x1=[1,2,3,4]
y1=[1,2,2,1]
plt.plot(x,y,color="red",linestyle="dashed")
plt.show()
######################
x1=[1,2,3,4]
y1=[1,2,2,1]
plt.plot(x,y,color="red",linewidth=5)
plt.show()
##################################
x1=[1,2,3,4]
y1=[1,2,2,1]
plt.plot(x,y,color="red",marker="s",
         markerfacecolor="green",markersize=5)
plt.show()
###################################
x1=[1,2,3,4]
y1=[1,2,2,1]
plt.plot(x1,y1,color="red",marker="s",
         markerfacecolor="black",
         linewidth=5,linestyle="dashed",
         markersize=10)
plt.show()
###############################
#bar plot customize
t=["2017","2018","2019"]
x=[1,2,3]
y=[1,5,3]
plt.bar(x,y,tick_label=t,width=0.7,
        color=["blue","red","yellow"])
plt.show()
###################################
#label edi
x=[1,2,3]
y=[15,23,3]
plt.plot(x,y)
plt.xlabel("X-axis",fontdict={"family":"serif",
                            "color":"red",
                            "weight":"bold",
                            "size":16})
plt.ylabel("y-axis",fontdict={"family":"bold italic",
                            "color":"blue",
                            "weight":"bold",
                            "size":30})
plt.title("x vs y",fontdict={"family":"serif",
                            "color":"red",
                            "weight":"bold",
                            "size":16})
plt.show()
#######################################################
#scatter plt
x=[1,2,3]
y=[15,23,3]
plt.scatter(x,y,marker="o",color="red")
plt.show()
################################
#scatter plt
x=[1,2,3]
y=[15,23,3]
plt.scatter(x,y,marker="s",color="red")
plt.show()
##########################################
#college
s=["books","fees","bus_rent"]
p=[5000,15000,3000]
c=["r","y","b"]
plt.pie(p,labels=s,colors=c,shadow=True,startangle=90,
        explode=(0.1,0.1,0.4),
        radius=0.8,autopct="%1.1f%%")
plt.show()
###########################################
#college
s=["books","fees","bus_rent"]
p=[5000,15000,3000]
c=["r","y","b"]
plt.pie(p,labels=s,colors=c,shadow=True,
        startangle=90,explode=(0.1,0.3,0.5),
        radius=0.8,autopct="%1.1f%%")
plt.show()

########################################
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[100,200,300,400,500]
plt.bar(x,y)
plt.show()

