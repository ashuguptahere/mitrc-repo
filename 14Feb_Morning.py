#import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
le=preprocessing.LabelEncoder()

data=pd.read_csv(r"C:\Users\fluXcapacit0r\Desktop\ibm hr.csv")

data.info()
data["Attrition"]=le.fit_transform(data["Attrition"])
data["BusinessTravel"]=le.fit_transform(data["BusinessTravel"])
###########################################
d=[]
for i in data.columns:
    d.append(i)
print(d)
for i in d:
    from sklearn import preprocessing
    le=preprocessing.LabelEncoder()  
    data[i]=le.fit_transform(data[i])
####################################
for i in data.columns:
from sklearn import preprocessing
le=preprocessing.LabelEncoder()  
data[i]=le.fit_transform(data[i])

def Label_end(d):
    for i in d:
    from sklearn import preprocessing
    le=preprocessing.LabelEncoder()  
    data[i]=le.fit_transform(data[i])
#########################################
data=data.drop(["EmployeeCount",
                "EmployeeNumber",
                "Over18",
                "StandardHours"],axis=1)
data.info()
#########################################
y=data["Attrition"]
x=data.drop(["Attrition"],axis=1) 
#############################################
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,
                                test_size=.33,
                                random_state=42)

# total row =1470 train 67 test= 33
###model Decision Tree
from sklearn.tree import DecisionTreeClassifier
##########################
#model form
model=DecisionTreeClassifier()
#model train and try to fit on training data
model.fit(x_train,y_train)
#### model testing on test_data
y_pred=model.predict(x_test)
##################################################
from sklearn.metrics import accuracy_score
print("Model Accuracy is :",accuracy_score(y_test,y_pred))
#Model Accuracy is : 0.7901234567901234
from sklearn.metrics import confusion_matrix
print("Matrix is  :",confusion_matrix(y_test,y_pred))
###########################################################
##############graph visualization#########################
from sklearn import tree
with open(r"C:\Users\fluXcapacit0r\Desktop\model_tree.txt","w")as f:
    f=tree.export_graphviz(model,out_file=f)

    
###############################################################
import numpy as np
import pandas as pd
data=pd.read_excel(r"C:\Users\fluXcapacit0r\Desktop\data.xlsx",sheet_name="Sheet2")
d=[]
for i in data.columns:
    d.append(i)
print(d)
for i in d:
    from sklearn import preprocessing
    le=preprocessing.LabelEncoder()  
    data[i]=le.fit_transform(data[i]) 
data.info()
data.columns
data.pop("DAY ")  
############################NB########
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
# dep and ind sep
y=data['PLAY ']
x=data.drop(['PLAY '],axis=1)
#model fit
model.fit(x,y)
# model test condition
x_test=[0,1,0,1]
y_pred=model.predict([x_test,])
print("prediction is :",y_pred)












    
    
    
    
    
    
##############################################################
################NB#################################
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
######### NB#################
from sklearn.naive_bayes import GaussianNB
model=GaussianNB() 
#####model fit on x,y data
model.fit(x,y)
#########################################
def show(x_test):
    output=model.predict([x_test,])
    print("-"*50)
    print("We have three type of target :",
      data.target_names)
    print("prediction is on :",x_test)
    print("Prediction is :",data.target_names[output])
    print("-"*50)
#####################################################
sl=float(input("Enter Sepal Length :"))
sw=float(input("Enter Sepal Width :"))
pl=float(input("Enter Petal Length :"))
pw=float(input("Enter Petal Width :"))
x_test=[sl,sw,pl,pw]
show(x_test)