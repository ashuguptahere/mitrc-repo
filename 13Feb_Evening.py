from sklearn.datasets import load_iris
data=load_iris()
print(data)
print("Species of plant :",data.target_names)
x=data.data
y=data.target
#################################
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()
#model fit for training
model.fit(x,y)
###############################
x_test=[6.7,3.1,5.6,2.4]
op=model.predict([x_test,])
print("predicted speiecs is :",data.target_names[op])
##########################################
a=["6.7cm","3.1cm","5.6cm","2.4cm"]
f=[]
for i in a:
    d=i.split("c")
    f.append(float(d[0]))
print(f)
##############################################
###############SVM################
from sklearn.datasets import load_iris
data=load_iris()
print(data)
print("Species of plant :",data.target_names)
x=data.data
y=data.target
#################################
from sklearn.svm import SVC
model=SVC()
#model fit for training
model.fit(x,y)
###############################
x_test=[6.7,3.1,5.6,2.4]
op=model.predict([x_test,])
print("predicted speiecs is :",data.target_names[op])
###########################################
##########################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv(r"C:\Users\fluXcapacit0r\Desktop\Social_Network_Ads.csv")

data.columns
data.pop("User ID")
data.columns
################################################
data.isnull().sum()
data["EstimatedSalary"].plot.hist()
data["EstimatedSalary"].fillna(
        data["EstimatedSalary"].median(),
        inplace=True)
################################################
data["Age"].plot.hist()
data["Age"].fillna(
        data["Age"].mean(),
        inplace=True)
################################################
data.isnull().sum()
################################################
y=data["Purchased"]
x=data.drop(["Purchased"],axis=1)

from sklearn import preprocessing
le=preprocessing.LabelEncoder()
x["Gender"]=le.fit_transform(x["Gender"])

label_purchased=["UNPURCHASED","PURCHASED"]
lable_val=[0,1]

from sklearn.svm import SVC
model=SVC()
model.fit(x,y)

def pred(x_test):
    y_pred=model.predict([x_test,])
    ind=lable_val.index(y_pred)
    print("Prediction is :",label_purchased[ind])

g=int(input("Enter Gender as per 1: MALE 0: FEMALE :" ))
a=float(input("Enter Age :"))
es=float(input("Enter Salary :"))
x_test=[g,a,es]
pred(x_test)

    

    
    







