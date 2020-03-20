import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
data=load_iris()
##############################
print(data)
print(data.target_names)
print(data.data)
##############################
#dep and indep var
y=data.target
x=data.data
###################################
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()
#####model fit on x,y data
model.fit(x,y)
#######################
x_pred=[2,2,4,2]
output=model.predict([x_pred,])

print("-"*50)
print("We have three type of target :",
      data.target_names)
print("prediction is on :",x_pred)
print("Prediction is :",data.target_names[output])
print("-"*50)
###########################################
def show(x_test):
    output=model.predict([x_test,])
    print("-"*50)
    print("We have three type of target :",
      data.target_names)
    print("prediction is on :",x_test)
    print("Prediction is :",data.target_names[output])
    print("-"*50)
    
sl=float(input("Enter Sepal Length :"))
sw=float(input("Enter Sepal Width :"))
pl=float(input("Enter Petal Length :"))
pw=float(input("Enter Petal Width :"))
x_test=[sl,sw,pl,pw]
show(x_test)

#############################################
###########SVM####################
from sklearn.datasets import load_iris
data=load_iris()
##############################
print(data)
print(data.target_names)
print(data.data)
##############################
#dep and indep var
y=data.target
x=data.data
from sklearn.svm import SVC
model=SVC()
#####model fit on x,y data
model.fit(x,y)

def show(x_test):
    output=model.predict([x_test,])
    print("-"*50)
    print("We have three type of target :",
      data.target_names)
    print("prediction is on :",x_test)
    print("Prediction is :",data.target_names[output])
    print("-"*50)
    
sl=float(input("Enter Sepal Length :"))
sw=float(input("Enter Sepal Width :"))
pl=float(input("Enter Petal Length :"))
pw=float(input("Enter Petal Width :"))
x_test=[sl,sw,pl,pw]
show(x_test)
########################################
#########################################
import pandas as pd
import numpy as np
d=pd.read_csv(r"C:\Users\fluXcapacit0r\Desktop\Social_Network_Ads.csv")

d.info()
d.pop("User ID")
d.info()
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
d["Gender"]=le.fit_transform(d["Gender"])

y=d["Purchased"]
x=d.drop(["Purchased"],axis=1)

x.isnull().sum()
x["Age"].plot.hist()
x["Age"].fillna(x["Age"].mean(),inplace=True)

x["EstimatedSalary"].plot.hist()
x["EstimatedSalary"].fillna(x["EstimatedSalary"].median(),inplace=True)

from sklearn.svm import SVC
model=SVC()
#####model fit on x,y data
model.fit(x,y)
Y_label=["Pruchased","Not Purchased"]
Y_label_val=[1,0]

x_pred=[1,23,15000]
output=model.predict([x_pred,])
print(type(output))
ind=Y_label_val.index(output)
print("-"*50)
print("We have three type of target :",
      Y_label)
print("prediction is on :",x_pred)
print("Prediction is :",Y_label[ind])
print("-"*50)
##############################
d=[]
arr=["10meter","15meter","07meter"]
for i in arr:
    d.append(float(i[0:2]))
print(d)
################################
d=[]
arr=["10meter","15meter","077meter"]
for i in arr:
     y=i.split("m")
     d.append(float(y[0]))
print(d)